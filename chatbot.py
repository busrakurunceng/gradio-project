# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:46:25 2025

@author: busra
"""
import gradio as gr
from datetime import datetime

# Örnek bot cevapları
bot_responses = {
    "hello": "Hi there! 😊 How can I help you today?",
    "how are you?": "I'm doing great, thank you for asking! 😄",
    "bye": "Goodbye! 👋 Have a great day!",
}

# Basit chatbot fonksiyonu
def chat_function(message, chat_history):
    # Mesajı küçük harfe çeviriyoruz, böylece cevaplar daha kolay eşleşiyor
    message_lower = message.lower()

    # Bot'un cevabını bulma
    if message_lower in bot_responses:
        llm_response = bot_responses[message_lower]
    else:
        llm_response = "I'm sorry, I didn't understand that. 🤔"

    # Mesajları ve bot cevabını geçmişe ekle
    chat_history.append(("User", message))
    chat_history.append(("Bot", llm_response))

    return chat_history

# Gradio arayüzü oluşturuluyor
with gr.Blocks() as demo:
    gr.Markdown("### Basit Chatbot 🤖💬")

    # Sohbet geçmişini tutacak alan
    chat_history = gr.Chatbot(label="Chat History")

    # Kullanıcıdan gelen mesajı almak için Textbox
    input_textbox = gr.Textbox(label="Send a message", placeholder="Type here...", elem_classes=["input-field"])

    # Mesaj göndermek için Buton
    send_button = gr.Button("Send Message", elem_classes=["send-button"])

    # Mesajı ve geçmişi güncellemek için button click eventi
    send_button.click(fn=chat_function, inputs=[input_textbox, chat_history], outputs=[chat_history])

# Stil eklemek için CSS
css = """
    #chat-history {
        height: 400px;
        overflow-y: scroll;
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .input-field {
        background-color: #f0f0f0;
        border-radius: 8px;
        padding: 12px;
        font-size: 16px;
        width: 100%;
        margin: 10px 0;
    }

    .send-button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
        margin-top: 10px;
    }

    .send-button:hover {
        background-color: #45a049;
    }

    .gr-chatbot .message.user {
        background-color: #e6f7ff;
        border-radius: 10px;
        padding: 10px;
        color: #333;
        margin: 10px 0;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }

    .gr-chatbot .message.bot {
        background-color: #d1f7d1;
        border-radius: 10px;
        padding: 10px;
        color: #333;
        margin: 10px 0;
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
"""

# Arayüze stil ekliyoruz
demo.css = css

# Arayüzü başlat
demo.launch()

