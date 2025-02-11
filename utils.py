from models import chatbot_model, translator, sentiment_analyzer

def generate_response(user_input):
    response = chatbot_model(user_input, pad_token_id=50256, eos_token_id=50256)
    return response[0]["generated_text"]

def translate_to_french(text):
    translated_text = translator(text)
    return translated_text[0]["translation_text"]

def analyze_sentiment(text):
    sentiment = sentiment_analyzer(text)
    sentiment_text = sentiment[0]["label"]
    sentiment_value = int(sentiment_text.split()[0])
    # Définition du sentiment global
    if sentiment_value <= 2:
        sentiment_class = "Négatif 😞"
    elif sentiment_value == 3:
        sentiment_class = "Neutre 😐"
    else:
        sentiment_class = "Positif 😊"
        
    return sentiment_class
    