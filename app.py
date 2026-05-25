from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = {
    "auto": "Auto Detect",
    "english": "English",
    "urdu": "Urdu",
    "arabic": "Arabic",
    "french": "French",
    "spanish": "Spanish",
    "german": "German",
    "italian": "Italian",
    "hindi": "Hindi",
    "turkish": "Turkish",
    "chinese (simplified)": "Chinese",
    "japanese": "Japanese",
    "korean": "Korean"
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    input_text = ""
    source_lang = "auto"
    target_lang = "urdu"
    error = ""

    if request.method == "POST":
        input_text = request.form.get("input_text", "").strip()
        source_lang = request.form.get("source_lang", "auto")
        target_lang = request.form.get("target_lang", "urdu")

        if not input_text:
            error = "Please enter text to translate."
        else:
            try:
                translated_text = GoogleTranslator(
                    source=source_lang,
                    target=target_lang
                ).translate(input_text)
            except Exception as e:
                error = f"Translation failed. Please check your internet connection. Error: {e}"

    return render_template(
        "index.html",
        languages=LANGUAGES,
        input_text=input_text,
        translated_text=translated_text,
        source_lang=source_lang,
        target_lang=target_lang,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
