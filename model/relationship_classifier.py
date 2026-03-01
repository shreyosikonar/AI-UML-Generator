def classify_relationships(components):
    classes = components["classes"]
    relationships = []

    for i in range(len(classes)-1):
        relationships.append({
            "from": classes[i],
            "to": classes[i+1],
            "type": "Association"
        })

    return relationships