from deep_translator import GoogleTranslator
from flask import Blueprint, render_template, request
from models.language_model import LanguageModel

language_controller = Blueprint("translation", __name__)


@language_controller.route("/", methods=["GET"])
def home():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/", methods=["POST"])
def translate_text():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    translated_text = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated_text,
    )


@language_controller.route("/reverse", methods=["POST"])
def reverse_translate_text():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]

    translated_text = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=translated_text,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
