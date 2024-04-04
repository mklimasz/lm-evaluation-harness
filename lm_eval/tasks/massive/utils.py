import argparse
from typing import Dict

import datasets
import yaml
#
# Listed languages are part of the MASSIVE dataset.
# These correspond to dataset names (Subsets) on HuggingFace.
# This script generates a yaml file for each language.
# Prompts are automatically translated using NLLB-200 3.3B, num_beams=4,
# with a manual post-edit based on back-translation.
LANGUAGES = {
    "af-ZA": {
        "prefix": "Voorspel die voorneme van die uitspraak. Die moontlike keuses vir die voornemens is",
        "utt": "Uitspraak",
        "intent": "Voorneme",
    },
    "am-ET": {
        "prefix": "የንግግሩን ዓላማ አስቀድመው ይገምቱ. ለዓላማዎች ሊሆኑ የሚችሉ ምርጫዎች የሚከተሉት ናቸው",
        "utt": "ንግግር",
        "intent": "ዓላማ",
    },
    "ar-SA": {
        "prefix": "التنبؤ بقصد البيان. الخيارات المحتملة للنوايا هي",
        "utt": "البيان",
        "intent": "النوايا",
    },
    "az-AZ": {
        "prefix": "İfadənin niyyətini təxmin edin. Niyyətlər üçün mümkün seçimlər",
        "utt": "İfadə",
        "intent": "Niyyət",
    },
    "bn-BD": {
        "prefix": "অভিব্যক্তিটির অভিপ্রায় পূর্বাভাস দিন। অভিপ্রায়গুলির জন্য সম্ভাব্য পছন্দগুলি হল",
        "utt": "অভিব্যক্তি",
        "intent": "অভিপ্রায়",
    },
    "ca-ES": {
        "prefix": "Predicció de la intenció de l'expressió. Les opcions possibles per a les intencions són",
        "utt": "Expressió",
        "intent": "Intenció",
    },
    "cy-GB": {
        "prefix": "Dylid rhagweld bwriad y datganiad. Y dewisiadau posibl ar gyfer y bwriadau yw",
        "utt": "Datganiad",
        "intent": "Bwriad",
    },
    "da-DK": {
        "prefix": "Forudsige hensigten med udtalelsen. De mulige valg for hensigterne er",
        "utt": "Udtalelse",
        "intent": "Hensigt",
    },
    "de-DE": {
        "prefix": "Vorhersage der Absicht der Äußerung. Die möglichen Auswahlmöglichkeiten für die Absichten sind",
        "utt": "Äußerung",
        "intent": "Absicht",
    },
    "el-GR": {
        "prefix": "Προβλέψτε την πρόθεση της ομιλίας. Οι πιθανές επιλογές για τις προθέσεις είναι",
        "utt": "Ομιλία",
        "intent": "Πρόθεση",
    },
    "en-US": {
        "prefix": "Predict the intent of the utterance. The possible choices for the intents are",
        "utt": "Utterance",
        "intent": "Intent",
    },
    "es-ES": {
        "prefix": "Predicir la intención de la expresión. Las opciones posibles para las intenciones son",
        "utt": "Expresión",
        "intent": "Intención",
    },
    "fa-IR": {
        "prefix": "پیش بینی قصد بیان. انتخاب های ممکن برای اهداف عبارتند از",
        "utt": "بیان",
        "intent": "قصد",
    },
    "fi-FI": {
        "prefix": "Ennusta lausunnon tarkoitus. Tarkoitusten mahdolliset valinnat ovat",
        "utt": "Lausunto",
        "intent": "Tarkoitus",
    },
    "fr-FR": {
        "prefix": "Prédire l'intention de l'énoncé. Les choix possibles pour les intentions sont",
        "utt": "Enoncé",
        "intent": "Intent",
    },
    "he-IL": {
        "prefix": "תחזית כוונת ההצהרה. הבחירות האפשריות לכוונות הן",
        "utt": "ההצהרה",
        "intent": "כוונה",
    },
    "hi-IN": {
        "prefix": "कथन के इरादे की भविष्यवाणी करें. इरादों के लिए संभावित विकल्प हैं",
        "utt": "कथन",
        "intent": "इरादा",
    },
    "hu-HU": {
        "prefix": "Előrejelzi a kijelentés szándékát. A lehetséges választási lehetőségek a következők",
        "utt": "Kijelentés",
        "intent": "Szándék",
    },
    "hy-AM": {
        "prefix": "Ենթադրեք արտահայտության նպատակը. Նպատակների հնարավոր ընտրությունները հետեւյալն են",
        "utt": "արտահայտություն",
        "intent": "մտադրություն",
    },
    "id-ID": {
        "prefix": "Memprediksi maksud dari pernyataan. Pilihan yang mungkin untuk maksud adalah",
        "utt": "Ucapan",
        "intent": "Niat",
    },
    "is-IS": {
        "prefix": "Gera spá um ásetningu orðsins. Mögulegir valkostir fyrir ásetningarnar eru",
        "utt": "Orð",
        "intent": "Ásetning",
    },
    "it-IT": {
        "prefix": "Predire l'intento dell'espressione. Le scelte possibili per gli intents sono",
        "utt": "Espressione",
        "intent": "Intento",
    },
    "ja-JP": {
        "prefix": "発音の意図を予測する.発音の意図の選択肢は次のとおりである",
        "utt": "発音",
        "intent": "意図",
    },
    "jv-ID": {
        "prefix": "Prediksi maksud saka utterance. Pilihan sing bisa dipilih kanggo intents yaiku",
        "utt": "Utterance",
        "intent": "Intent",
    },
    "ka-GE": {
        "prefix": "პროგნოზირება განცხადების განზრახვის შესახებ. განზრახვის შესაძლო არჩევანი არის",
        "utt": "განცხადება",
        "intent": "განზრახვა",
    },
    "km-KH": {
        "prefix": "ទស្សន៍ទាយគោលបំណងនៃសំដី។ ជម្រើសដែលអាចធ្វើបានសម្រាប់គោលបំណងគឺ",
        "utt": "សំដី",
        "intent": "គោលបំណង",
    },
    "kn-IN": {
        "prefix": "ಉಚ್ಚಾರಣೆಯ ಉದ್ದೇಶವನ್ನು ಊಹಿಸಿ. ಉಚ್ಚಾರಣೆಗಳಿಗೆ ಸಾಧ್ಯವಿರುವ ಆಯ್ಕೆಗಳು",
        "utt": "ಹೇಳಿಕೆ",
        "intent": "ಉದ್ದೇಶ",
    },
    "ko-KR": {
        "prefix": "표현의 의도를 예측합니다. 의도에 대한 가능한 선택은",
        "utt": "표현",
        "intent": "의도는",
    },
    "lv-LV": {
        "prefix": "Prognozēt izteiksmes nodomu. Ieteicamas izteiksmes nodomu izvēles i:",
        "utt": "Izteiksme",
        "intent": "Nodoms",
    },
    "ml-IN": {
        "prefix": "പ്രസ്താവനയുടെ ഉദ്ദേശ്യത്തെ പ്രവചിക്കുക. ഉദ്ദേശ്യങ്ങൾക്കായുള്ള സാധ്യമായ തിരഞ്ഞെടുപ്പുകൾ ഇവയാണ്",
        "utt": "പ്രസ്താവന",
        "intent": "ഉദ്ദേശം",
    },
    "mn-MN": {
        "prefix": "Урьдчилан таамаглах. Урьдчилан таамаглах боломжийн сонголт нь",
        "utt": "Хэлсэн үг",
        "intent": "Зорилго",
    },
    "ms-MY": {
        "prefix": "Ramalkan niat ucapan. Pilihan yang mungkin untuk niat adalah",
        "utt": "Ucapan",
        "intent": "Niat",
    },
    "my-MM": {
        "prefix": "စကားပြောဆိုမှု၏ ရည်ရွယ်ချက်ကို ခန့်မှန်းပါ။ ရည်ရွယ်ချက်များအတွက် ဖြစ်နိုင်ခြေရှိသည့် ရွေးချယ်မှုမျာ မှာ",
        "utt": "စကားပြော",
        "intent": "ရည်ရွယ်ချက်",
    },
    "nb-NO": {
        "prefix": "Forutsi intensjonen til uttalelsen. De mulige valgene for intensjonene er",
        "utt": "Uttalelse",
        "intent": "Intensjon",
    },
    "nl-NL": {
        "prefix": "Voorspellen van de intentie van de uitspraak. De mogelijke keuzes voor de intenties zijn",
        "utt": "Uitspraak",
        "intent": "Intentie",
    },
    "pl-PL": {
        "prefix": "Przewiduj intencję wypowiedzi. Możliwe wybory dla intencji to",
        "utt": "Wypowiedź",
        "intent": "Intencja",
    },
    "pt-PT": {
        "prefix": "Preveja a intenção do enunciado. As opções possíveis para os enunciados são",
        "utt": "Enunciado:",
        "intent": "Intenção:",
    },
    "ro-RO": {
        "prefix": "Prezice intenția enunțului. Opțiunile posibile pentru intenții sunt",
        "utt": "Enunț",
        "intent": "Intenția",
    },
    "ru-RU": {
        "prefix": "Предсказать намерение высказывания. Возможные варианты намерений",
        "utt": "Высказывание",
        "intent": "Намерение",
    },
    "sl-SL": {
        "prefix": "Predvidi namen izraza. Možne izbire za namere so",
        "utt": "Izraz",
        "intent": "Namera",
    },
    "sq-AL": {
        "prefix": "Parashikoni qëllimin e shprehjes. Zgjedhjet e mundshme për qëllimet janë",
        "utt": "Shprehje",
        "intent": "Qëllim",
    },
    "sv-SE": {
        "prefix": "Förutsäga uttalandets avsikt. De möjliga valmöjligheterna för avsikterna är",
        "utt": "Uttryck",
        "intent": "Avsikt",
    },
    "sw-KE": {
        "prefix": "Kutabiri nia ya kujieleza. uchaguzi inawezekana kwa ajili ya nia ni",
        "utt": "Kujieleza",
        "intent": "Nia",
    },
    "ta-IN": {
        "prefix": "உச்சரிப்பின் நோக்கத்தை முன்னறிவிக்கவும். நோக்கங்களுக்கான சாத்தியமான தேர்வுகள்",
        "utt": "உச்சரிப்பு",
        "intent": "நோக்கம்",
    },
    "te-IN": {
        "prefix": "ఉచ్చారణ యొక్క ఉద్దేశ్యాన్ని అంచనా వేయండి. ఉద్దేశ్యాల కోసం సాధ్యమైన ఎంపికలు",
        "utt": "ఉచ్చారణ",
        "intent": "ఉద్దేశ్యం",
    },
    "th-TH": {
        "prefix": "คาดเดาความตั้งใจของคําพูด ตัวเลือกที่เป็นไปได้สําหรับความตั้งใจคือ",
        "utt": "คําพูด",
        "intent": "ความตั้งใจ",
    },
    "tl-PH": {
        "prefix": "Hulaan ang intensyon ng pahayag. Ang mga posibleng pagpipilian para sa mga intensyon ay",
        "utt": "Pangungusap",
        "intent": "Intensyon",
    },
    "tr-TR": {
        "prefix": "İfadenin amacını tahmin edin. Amaçlar için olası seçenekler şunlardır",
        "utt": "İfade",
        "intent": "Niyet",
    },
    "ur-PK": {
        "prefix": "بیان کے ارادے کی پیش گوئی کریں۔ ارادوں کے لئے ممکنہ انتخاب یہ ہیں",
        "utt": "بیان",
        "intent": "ارادے",
    },
    "vi-VN": {
        "prefix": "Dự đoán ý định của phát biểu. Các lựa chọn có thể cho các ý định là",
        "utt": "Phát biểu",
        "intent": "Ý định",
    },
    "zh-CN": {
        "prefix": "预测语句的意图.意图的可能选择是",
        "utt": "语句",
        "intent": "意图",
    },
    "zh-TW": {
        "prefix": "預測發言的意圖. 發言的可能選擇是",
        "utt": "發言",
        "intent": "意圖",
    },
}


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    choices = dataset.features["intent"].names

    def _process_doc(doc: Dict) -> Dict:
        doc["choices"] = choices
        return doc

    return dataset.map(_process_doc)


def doc_to_text(doc: Dict) -> str:
    choices = ", ".join(doc["choices"][:-1]) + " and " + doc["choices"][-1]
    utterance = doc["utt"]
    prompt_parts = LANGUAGES[doc["locale"]]
    text = f"{prompt_parts['prefix']}: {choices}.\n\n{prompt_parts['utt']}: {utterance}\n{prompt_parts['intent']}:"
    return text


def doc_to_target(doc: Dict) -> str:
    choices = doc["choices"]
    target_idx = doc["intent"]
    return choices[target_idx]


def gen_lang_yamls(output_dir: str, overwrite: bool) -> None:
    """
    Generate a yaml file for each language.

    :param output_dir: The directory to output the files to.
    :param overwrite: Whether to overwrite files if they already exist.
    """
    err = []
    for lang in LANGUAGES.keys():
        file_name = f"massive_intent_{lang}.yaml"
        try:
            with open(
                    f"{output_dir}/{file_name}", "w" if overwrite else "x", encoding="utf-8"
            ) as f:
                f.write("# Generated by utils.py\n")
                yaml.dump(
                    {
                        "include": "massive_intent_common_yaml",
                        "dataset_name": lang,
                        "task": f"massive_intent_{lang}",
                    },
                    f,
                )
        except FileExistsError:
            err.append(file_name)

    if len(err) > 0:
        raise FileExistsError(
            "Files were not created because they already exist (use --overwrite flag):"
            f" {', '.join(err)}"
        )


def main() -> None:
    """Parse CLI args and generate language-specific yaml files."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--overwrite",
        default=False,
        action="store_true",
        help="Overwrite files if they already exist",
    )
    parser.add_argument(
        "--output-dir", default=".", help="Directory to write yaml files to"
    )
    args = parser.parse_args()

    gen_lang_yamls(output_dir=args.output_dir, overwrite=args.overwrite)


if __name__ == "__main__":
    main()
