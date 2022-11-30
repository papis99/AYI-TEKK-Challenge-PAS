import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import json

nlp = spacy.load("fr_core_news_sm")
matcher = Matcher(nlp.vocab)

pattern1 = [{"LOWER": "ostéosarcome"}]
pattern2 = [{"LOWER": "fièvre"}, {"POS": "NOUN", "OP": "?"}]
pattern3 = [{"LOWER": "fièvre"}, {"POS": "ADJ", "OP": "?"}]
pattern4 = [{"LOWER": "frissons"}]
pattern5 = [{"LOWER": "hyperthermie"}]
pattern6 = [{"LOWER": "hyperthermies"}]
pattern7 = [{"LOWER": "coma"}]
pattern8 = [{"LOWER": "hématurie"}]
pattern9 = [{"LOWER": "rectorragies"}]
pattern10 = [{"LOWER": "rectorragie"}]
pattern11 = [{"LOWER": "mélénas"}]
pattern12 = [{"LOWER": "méléna"}]
pattern13 = [{"LOWER": "vomissements"}]
pattern14 = [{"LOWER": "vomissement"}]
pattern15 = [{"LOWER": "fébrile"}]
pattern16 = [{"LOWER": "ecchymose"}]
pattern17 = [{"LOWER": "ecchymoses"}]
pattern18 = [{"LOWER": "tumeur"}]
pattern19 = [{"LOWER": "tumeurs"}]
pattern20 = [{"LOWER": "kyste"}]
pattern21 = [{"LEMMA": "violer"}]
pattern22 = [{"LOWER": "inconscient"}]
pattern23 = [{"LOWER": "agitation"}]
pattern24 = [{"LOWER": "hypersomnie"}]
pattern25 = [{"LOWER": "insomnie"}]
pattern26 = [{"LOWER": "céphalées"}]
pattern27 = [{"LOWER": "céphalée"}]
pattern28 = [{"LOWER": "palpitations"}]
pattern29 = [{"LOWER": "palpitation"}]
pattern30 = [{"LOWER": "atrophie"}]
pattern31 = [{"LOWER": "malaise"}]
pattern32 = [{"LOWER": "paludisme"}]
pattern33 = [{"LOWER": "sida"}]
pattern34 = [{"LOWER": "tuberculose"}]
pattern35 = [{"LOWER": "méningite"}]
pattern36 = [{"LOWER": "grippe"}]
pattern37 = [{"LOWER": "infection"}, {"LOWER": "urinaire"}]
pattern38 = [{"LOWER": "infection"}, {"POS": "NOUN", "OP": "?"}]
pattern39 = [{"LOWER": "hypotension"}, {"LOWER": "artérielle"}]
pattern40 = [{"LOWER": "hypertension"}, {"POS": "NOUN", "OP": "?"}]
pattern41 = [{"LOWER": "hypotension"}, {"POS": "NOUN", "OP": "?"}]
pattern42 = [{"LOWER": "hypertension"}, {"LOWER": "artérielle"}]
pattern43 = [{"LOWER": "leucémie"}, {"POS": "NOUN", "OP": "*"}]
pattern44 = [{"LOWER": "constipation"}, {"POS": "NOUN", "OP": "*"}]
pattern45 = [{"LOWER": "brûlures"}, {"POS": "NOUN", "OP": "*"}]
pattern46 = [{"LOWER": "brûlure"}, {"POS": "NOUN", "OP": "*"}]
pattern47 = [{"LOWER": "crises"}, {"POS": "NOUN", "OP": "*"}]
pattern48 = [{"LOWER": "crise"}, {"POS": "NOUN", "OP": "*"}]
pattern49 = [{"LOWER": "traumatisme"}, {"POS": "NOUN", "OP": "*"}]
pattern50 = [{"LOWER": "écoulement"}, {"POS": "NOUN", "OP": "*"}]
pattern51 = [{"LOWER": "lésions"}, {"POS": "NOUN", "OP": "*"}]
pattern52 = [{"LOWER": "lésion"}, {"POS": "NOUN", "OP": "*"}]
pattern53 = [{"POS": "NOUN", "OP": "?"}, {"LOWER": "hépatiques"}]
pattern54 = [{"POS": "NOUN", "OP": "?"}, {"LOWER": "hépatique"}]
pattern55 = [{"POS": "ADJ", "OP": "?"}, {"LOWER": "hépatiques"}]
pattern56 = [{"POS": "ADJ", "OP": "?"}, {"LOWER": "hépatique"}]
pattern57 = [{"LOWER": "ostéosarcome"}, {"LOWER": "du", "OP": "?"}, {"LOWER": "fémur"}]
pattern58 = [{"LOWER": "ostéosarcome"}, {"LOWER": "du", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern59 = [{"LOWER": "douleurs"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "ADJ", "OP": "*"}]
pattern60 = [{"LOWER": "douleurs"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern61 = [{"LOWER": "douleur"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "ADJ", "OP": "*"}]
pattern62 = [{"LOWER": "douleur"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern63 = [{"LOWER": "troubles"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "ADJ", "OP": "*"}]
pattern64 = [{"LOWER": "troubles"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern65 = [{"LOWER": "trouble"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "ADJ", "OP": "*"}]
pattern66 = [{"LOWER": "trouble"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern67 = [{"LOWER": "mal"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN"}]
pattern68 = [{"LOWER": "mal"}, {"LOWER": "à", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN"}]
pattern69 = [{"LOWER": "maux"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN"}]
pattern70 = [{"LEMMA": "kyste"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "?"}]
pattern71 = [{"LEMMA": "kyste"}, {"LOWER": "du", "OP": "?"}, {"POS": "NOUN", "OP": "?"}]
pattern72 = [{"LOWER": "probléme"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern73 = [{"LOWER": "probléme"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "ADJ", "OP": "*"}]
pattern74 = [{"LOWER": "problémes"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "NOUN", "OP": "*"}]
pattern75 = [{"LOWER": "problémes"}, {"LOWER": "de", "OP": "?"}, {"LOWER": "la", "OP": "?"}, {"POS": "ADJ", "OP": "*"}]
pattern76 = [{"LOWER": "malade"}]
pattern77 = [{"LOWER": "diarrhée"}]

# Ajoute le motif au matcher
matcher.add("Diagnostic",
            [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7, pattern8, pattern9, pattern10,
             pattern11, pattern12, pattern13, pattern14, pattern15, pattern16, pattern17, pattern18, pattern19,
             pattern20, pattern21, pattern22, pattern23, pattern24, pattern25, pattern26, pattern27, pattern28,
             pattern29, pattern30, pattern31, pattern32, pattern33, pattern34, pattern35, pattern36, pattern37,
             pattern38, pattern39, pattern40, pattern41, pattern42, pattern43, pattern44, pattern45, pattern46,
             pattern47, pattern48, pattern49, pattern50, pattern51, pattern52, pattern53, pattern54, pattern55,
             pattern56, pattern57, pattern58, pattern59, pattern60, pattern61, pattern62, pattern63, pattern64,
             pattern65, pattern66, pattern67, pattern68, pattern69, pattern70, pattern71, pattern72, pattern73,
             pattern74, pattern75, pattern76, pattern77])


def recup_texte(TEXT):
    doc = nlp(TEXT)
    ents = []
    # Itère sur les correspondances
    for match_id, start, end in matcher(doc):
        # print(start)
        # Crée un Span avec le label pour "Age"
        span = Span(doc, start, end, label="Diagnostic")
        # Actualise doc.ents avec l'ajout du span
        ents = list(ents) + [span]
        # print([(ent.text) for ent in doc.ents])
    return ents