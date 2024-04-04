# Task-name

### Paper

Title: `MASSIVE 1.1: A 1M-Example Multilingual Natural Language Understanding Dataset with 52 Typologically-Diverse Languages`

Abstract: `https://aclanthology.org/2023.acl-long.235.pdf`

`MASSIVE 1.1 is a parallel dataset of > 1M utterances across 52 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types. MASSIVE was created by localizing the SLURP dataset, composed of general Intelligent Voice Assistant single-shot interactions.`

Homepage: `https://github.com/alexa/massive`


### Citation

```
@inproceedings{fitzgerald-etal-2023-massive,
    title = "{MASSIVE}: A 1{M}-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-Diverse Languages",
    author = "FitzGerald, Jack  and
      Hench, Christopher  and
      Peris, Charith  and
      Mackie, Scott  and
      Rottmann, Kay  and
      Sanchez, Ana  and
      Nash, Aaron  and
      Urbach, Liam  and
      Kakarala, Vishesh  and
      Singh, Richa  and
      Ranganath, Swetha  and
      Crist, Laurie  and
      Britan, Misha  and
      Leeuwis, Wouter  and
      Tur, Gokhan  and
      Natarajan, Prem",
    editor = "Rogers, Anna  and
      Boyd-Graber, Jordan  and
      Okazaki, Naoaki",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.235",
    doi = "10.18653/v1/2023.acl-long.235",
    pages = "4277--4302",
    abstract = "We present the MASSIVE dataset{--}Multilingual Amazon Slu resource package (SLURP) for Slot-filling, Intent classification, and Virtual assistant Evaluation. MASSIVE contains 1M realistic, parallel, labeled virtual assistant utterances spanning 51 languages, 18 domains, 60 intents, and 55 slots. MASSIVE was created by tasking professional translators to localize the English-only SLURP dataset into 50 typologically diverse languages from 29 genera. We also present modeling results on XLM-R and mT5, including exact match accuracy, intent classification accuracy, and slot-filling F1 score. We have released our dataset, modeling code, and models publicly.",
}

@inproceedings{bastianelli-etal-2020-slurp,
    title = "{SLURP}: A Spoken Language Understanding Resource Package",
    author = "Bastianelli, Emanuele  and
      Vanzo, Andrea  and
      Swietojanski, Pawel  and
      Rieser, Verena",
    editor = "Webber, Bonnie  and
      Cohn, Trevor  and
      He, Yulan  and
      Liu, Yang",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.emnlp-main.588",
    doi = "10.18653/v1/2020.emnlp-main.588",
    pages = "7252--7262",
    abstract = "Spoken Language Understanding infers semantic meaning directly from audio data, and thus promises to reduce error propagation and misunderstandings in end-user applications. However, publicly available SLU resources are limited. In this paper, we release SLURP, a new SLU package containing the following: (1) A new challenging dataset in English spanning 18 domains, which is substantially bigger and linguistically more diverse than existing datasets; (2) Competitive baselines based on state-of-the-art NLU and ASR systems; (3) A new transparent metric for entity labelling which enables a detailed error analysis for identifying potential areas of improvement. SLURP is available at \url{https://github.com/pswietojanski/slurp}.",
}
```

### Groups and Tasks

#### Groups

* `massive_intent`: `Prompt format is based on bigbench/intent_recognition`

#### Tasks

* `massive_intent_af-ZA`
* `massive_intent_am-ET`
* `massive_intent_ar-SA`
* `massive_intent_az-AZ`
* `massive_intent_bn-BD`
* `massive_intent_ca-ES`
* `massive_intent_cy-GB`
* `massive_intent_da-DK`
* `massive_intent_de-DE`
* `massive_intent_el-GR`
* `massive_intent_en-US`
* `massive_intent_es-ES`
* `massive_intent_fa-IR`
* `massive_intent_fi-FI`
* `massive_intent_fr-FR`
* `massive_intent_he-IL`
* `massive_intent_hi-IN`
* `massive_intent_hu-HU`
* `massive_intent_hy-AM`
* `massive_intent_id-ID`
* `massive_intent_is-IS`
* `massive_intent_it-IT`
* `massive_intent_ja-JP`
* `massive_intent_jv-ID`
* `massive_intent_ka-GE`
* `massive_intent_km-KH`
* `massive_intent_kn-IN`
* `massive_intent_ko-KR`
* `massive_intent_lv-LV`
* `massive_intent_ml-IN`
* `massive_intent_mn-MN`
* `massive_intent_ms-MY`
* `massive_intent_my-MM`
* `massive_intent_nb-NO`
* `massive_intent_nl-NL`
* `massive_intent_pl-PL`
* `massive_intent_pt-PT`
* `massive_intent_ro-RO`
* `massive_intent_ru-RU`
* `massive_intent_sl-SL`
* `massive_intent_sq-AL`
* `massive_intent_sv-SE`
* `massive_intent_sw-KE`
* `massive_intent_ta-IN`
* `massive_intent_te-IN`
* `massive_intent_th-TH`
* `massive_intent_tl-PH`
* `massive_intent_tr-TR`
* `massive_intent_ur-PK`
* `massive_intent_vi-VN`
* `massive_intent_zh-CN`
* `massive_intent_zh-TW`

### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
    * [ ] Have you referenced the original paper that introduced the task?
    * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [ ] Is the "Main" variant of this task clearly denoted?
* [ ] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [ ] Have you noted which, if any, published evaluation setups are matched by this variant?
