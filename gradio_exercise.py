# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:26:20 2025

@author: busra
"""

import gradio as gr
import tensorflow as tf
import numpy as np
import request
import pandas as pd
import math

#%%
#Basic Interface

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn = greet, inputs="text" , outputs="text")
demo.launch()

#%%

#TextBox

def reverse_text(text):
    return text[::-1]

demo = gr.Interface(fn=reverse_text, inputs=gr.Textbox(), outputs="text")
demo.launch()


def count_number_of_words(text):
    words = text.split()  # Split the text by spaces
    count = len(words)    # Count the number of words
    return f"Word count: {count}"
    
demo = gr.Interface(fn=count_number_of_words, inputs="text", outputs="text")
demo.launch()

#%%
#Number Input
def square(num):
    return num * num

demo = gr.Interface(fn=square, inputs=gr.Number(), outputs="number")
demo.launch()

def cube(num):
    return num * num * num

demo = gr.Interface(fn=cube, inputs=gr.Number(), outputs="number")
demo.launch()

#%%
#Slider

def multiply(value):
    return value * 10

demo = gr.Interface(fn=multiply, inputs=gr.Slider(minimum=1, maximum=100), outputs="number")
demo.launch()

def square_root(value):
    root = math.sqrt(value)
    return root

demo = gr.Interface(fn=square_root, inputs=gr.Slider(minimum=1, maximum=100), outputs="number")
demo.launch()

#%%
#Drapdown

def get_color(color):
    return f"You selected: {color}"

demo = gr.Interface(fn=get_color, inputs=gr.Dropdown(choices=["Red", "Green", "Blue"]), outputs="emojies")
demo.launch()

#%%
#Radio Buttons

def favorite_fruit(fruit):
    return f"Nice choice! {fruit} is tasty 🍏"

demo = gr.Interface(fn=favorite_fruit, inputs=gr.Radio(choices=["Apple", "Banana", "Cherry" ,"Cucumber", "Orange", "Grapes"]), outputs="text")
demo.launch()

#%%
# Checkbox & CheckboxGroup

def show_languages(languages):
    return f"You selected: {', '.join(languages)}"

demo = gr.Interface(fn=show_languages, inputs=gr.CheckboxGroup(choices=["Python", "Java", "C++"]), outputs="text")
demo.launch()

#%%

#Output Components

def sentiment_analysis(text):
    
    if "happy" in text.lower():
        answer = "Positive 😊"
    elif "sad" in text.lower():
        answer = "Negative 😞"
    else: 
        answer = "Neutral 😐"
    return answer 

demo = gr.Interface(fn=sentiment_analysis, inputs="text", outputs=gr.Label())
demo.launch()


#%%

def generate_image():
    return np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

demo = gr.Interface(fn=generate_image, inputs=None, outputs="image")
demo.launch()

#%%
#Audio Output 
def generate_audio():
    return "example_audio.wav"

demo = gr.Interface(fn=generate_audio, inputs=None, outputs="audio")
demo.launch()

#%%
# File Upload & Download 

def file_info(file):
    return f"Received file: {file.name}"

demo = gr.Interface(fn=file_info, inputs="file", outputs="text")
demo.launch()


#%%

def format_text(text, case, length):
    if case == "Uppercase":
        text = text.upper()
    elif case == "Lowercase":
        text = text.lower()
    
    return text[:length]  # Trim the text based on the slider value

demo = gr.Interface(
    fn=format_text,
    inputs=[
        gr.Textbox(label="Enter Text"),
        gr.Dropdown(choices=["Uppercase", "Lowercase"], label="Select Format"),
        gr.Slider(minimum=1, maximum=100, value=50, label="Trim Length")
    ],
    outputs="text"
)

demo.launch()

#%%

def greet(name):
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("# Welcome to Gradio Blocks! 🎉")  # Title
    textbox = gr.Textbox(label="Enter your name")
    button = gr.Button("Greet")
    output = gr.Textbox(label="Greeting Message")

    button.click(greet, inputs=textbox, outputs=output)  # Connect function

demo.launch()





