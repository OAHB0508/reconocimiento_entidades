# API de Reconocimiento de Entidades Nombradas (NER) en Español

Esta API es una aplicación web sencilla desarrollada con Flask y spaCy que permite identificar entidades nombradas en oraciones en español. 
La API acepta solicitudes POST y devuelve una lista de las entidades identificadas junto con el tipo de cada entidad.

## Configuración del Entorno

Para ejecutar la API, sigue estos pasos:

1. Crea un entorno virtual:
	conda create --name ner-api python=3.8
	conda activate ner-api

2. Instalar dependencias necesarias 
	pip install Flask
	pip install spacy

	python -m spacy download es_core_news_sm

3. Ejecutar aplicación
	python app.py
La API estará disponible en http://127.0.0.1:5000/ner

4. Enviar Solicitud  POST (En mi caso probe con postman)
Envía una solicitud POST con un JSON que contiene una lista de oraciones en español:
curl -X POST -H "Content-Type: application/json" -d '{
  "oraciones": [
    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera."
  ]
}' http://127.0.0.1:5000/ner

5. Respuesta de API
La API devolverá una respuesta en formato JSON que contiene las entidades nombradas identificadas en cada oración junto con su tipo. 
Por ejemplo:
{	
  "resultado": [
    {
      "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
      "entidades": {
        "Apple": "ORG",
        "Reino Unido": "LOC"
      }
    },
    {
      "oración": "San Francisco considera prohibir los robots de entrega en la acera.",
      "entidades": {
        "San Francisco": "LOC"
      }
    }
  ]
}
