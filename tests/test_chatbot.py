import os
from transformers import pipeline
from dotenv import load_dotenv

# Charger les variables depuis le fichier .env
load_dotenv()

# Récupérer le token Hugging Face
TOKEN_KEY = os.getenv("HF_TOKEN_KEY")
assert TOKEN_KEY is not None, "❌ ERREUR : TOKEN_KEY n'est pas défini dans l'environnement !"

# Définir la fonction de traduction indépendamment du module `utils`
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr", use_auth_token=TOKEN_KEY)

def translate_to_french(text):
    translated_text = translator(text)
    return translated_text[0]["translation_text"]

# Test unitaire de la fonction
def test_translation():
    result = translate_to_french("Hello")
    assert result.lower().strip() == "bonjour", f"Résultat inattendu : {result}"
