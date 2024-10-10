from flask import Flask, request, jsonify
from flask_cors import CORS
from fpdf import FPDF
import json
import os

app = Flask(__name__)
CORS(app, resources={r"/submit": {"origins": "*"}})


SAVE_DIR = r'C:\Users\j.batthauer\Documents\Checklistenprotokolle Arbeitsplatz- und Anlageneinrichtung'

@app.route('/submit', methods=['POST'])
def save_checklist():
    data = request.get_json()  # Formulardaten auslesen
    print("Daten empfangen:", data)

    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)  # Erstelle Ordner, falls nicht vorhanden
        print("Ordner erstellt:", SAVE_DIR)

    # Erstelle eine PDF-Datei
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Füge die Formulardaten der PDF hinzu
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    # Speichere die PDF-Datei
    file_path = os.path.join(SAVE_DIR, 'checkliste.pdf')
    pdf.output(file_path)
    
    print("PDF gespeichert unter:", file_path)
    return jsonify({"message": "Checkliste erfolgreich gespeichert!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

