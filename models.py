from transformers import pipeline
from config import Config

# Modèle de chatbot (DialoGPT)
chatbot_model = pipeline("text-generation", model="microsoft/DialoGPT-medium", token=Config.TOKEN_KEY)

# Modèle de traduction français -> anglais
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-fr-en", token=Config.TOKEN_KEY)

# Modèle d'analyse de sentiment
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", token=Config.TOKEN_KEY)
