import spacy

nlp = spacy.load("en_core_web_sm")

def extract_uml_components(text):
    doc = nlp(text)

    classes = []
    attributes = []
    methods = []

    for token in doc:
        if token.pos_ == "NOUN":
            classes.append(token.text.capitalize())
        elif token.pos_ == "ADJ":
            attributes.append(token.text)
        elif token.pos_ == "VERB":
            methods.append(token.lemma_)

    return {
        "classes": list(set(classes)),
        "attributes": list(set(attributes)),
        "methods": list(set(methods))
    }