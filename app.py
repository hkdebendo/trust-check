from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

from models.text_model import detect_abusive
from models.image_model import check_image

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyze_text", methods=["POST"])
def analyze_text():
    text = request.form.get("text", "").strip()
    if text == "":
        return jsonify({"error": "Texte vide"}), 400

    result = detect_abusive(text)
    return jsonify(result)

@app.route("/analyze_image", methods=["POST"])
def analyze_image():
    if "image" not in request.files:
        return jsonify({"error": "Aucun fichier uploadé"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "Nom de fichier vide"}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    result = check_image(path)

    # Optionnel : supprimer le fichier après analyse
    # os.remove(path)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
