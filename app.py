import gradio as gr
from utils import translate_to_french, analyze_sentiment, generate_response
from config import Config
from transformers import pipeline

def chatbot_response(user_input, history):
    translated = translate_to_french(user_input)
    sentiment = analyze_sentiment(translated)
    bot_response = generate_response(user_input)
    return f"Message Original : {user_input} \n Traduction Française : {translated} \n Sentiment : {sentiment} \n Réponse du chat : {bot_response}"

interface = gr.ChatInterface(chatbot_response, type="messages")

# Lancer l'application
if __name__ == "__main__":
    interface.launch()