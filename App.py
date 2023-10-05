from flask import Flask, jsonify, request
import spacy

app = Flask(__name__)
#Modelo a utilizar solicitado
nlp = spacy.load("es_core_news_sm")

@app.route('/ner',methods=['POST'])


def named_entity_recognition():
    if request.method == 'GET':
        return 

    if request.method == 'POST':
        try:
            data = request.get_json()
            sentences = data.get('oraciones', [])
            results = []

            for sentence in sentences:
                doc = nlp(sentence)
                entities = {}

                for ent in doc.ents:
                    entities[ent.text] = ent.label_

                result = {
                    "oración": sentence,
                    "entidades": entities
                }
                results.append(result)

            return jsonify({"resultado": results})
        except Exception as e:
            return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)