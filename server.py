from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Verzeichnis, in dem die Checklisten gespeichert werden
SAVE_DIR = r'C:\Users\j.batthauer\Documents\Checklistenprotokolle Arbeitsplatz- und Anlageneinrichtung'  # Rohstring

@app.route('/submit', methods=['POST'])
def save_checklist():
    data = request.get_json()  # Formulardaten auslesen
    print ("Daten empfangen:", data)
    
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)  # Erstelle Ordner, falls nicht vorhanden
        print("Ordner erstellt:" , SAVE_DIR)

    # Speichere die Datei als JSON
    file_path = os.path.join(SAVE_DIR, 'checkliste.json')
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

        print("Datei gespeichert unter:" , file_path)

    return jsonify({"message": "Checkliste erfolgreich gespeichert!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
