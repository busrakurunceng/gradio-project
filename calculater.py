# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:32:19 2025

@author: busra
"""
import gradio as gr

# Define the calculation function
def calculate(operand1, operand2, operation):
    if operation == "+":
        return operand1 + operand2
    elif operation == "-":
        return operand1 - operand2
    elif operation == "*":
        return operand1 * operand2
    elif operation == "/":
        if operand2 != 0:
            return operand1 / operand2
        else:
            return "Error: Division by Zero"
    elif operation == "^2":
        return operand1 ** 2
    elif operation == "^3":
        return operand1 ** 3
    else:
        return "Unknown operation"

# Create a Gradio Blocks interface
with gr.Blocks() as demo:
    with gr.Row():
        # Operand 1 and Operand 2 inputs
        operand1 = gr.Number(label="Number 1", scale=1, interactive=True, elem_classes=["input-field"])
        operand2 = gr.Number(label="Number 2", scale=1, interactive=True, elem_classes=["input-field"])
    
    with gr.Row():
        # Operation selection
        operation = gr.Radio(choices=["+", "-", "*", "/", "^2", "^3"], label="Operation", elem_classes=["operation-radio"])
    
    with gr.Row():
        # Button to calculate
        calculate_btn = gr.Button("Calculate", elem_classes=["gr-button"])

    with gr.Row():
        # Output result box
        result = gr.Textbox(label="Result", elem_classes=["result-box"])

    # Define the action on button click
    calculate_btn.click(calculate, inputs=[operand1, operand2, operation], outputs=result)

# Add custom CSS styling to improve the design
css = """
    .input-field {
        background-color: #f0f0f0;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        width: 90%;
        margin: 10px auto;
    }
    
    .operation-radio {
        background-color: #f7f7f7;
        border-radius: 8px;
        padding: 10px;
        font-size: 18px;
        width: 90%;
        margin: 10px auto;
    }
    
    .result-box {
        background-color: #d3f8d3;
        border-radius: 8px;
        font-size: 18px;
        padding: 15px;
        width: 90%;
        margin: 20px auto;
        font-weight: bold;
        color: #2c7a2f;
    }
    
    .gr-button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        width: 50%;
        margin: 20px auto;
        display: block;
    }
    
    .gr-button:hover {
        background-color: #45a049;
    }
"""

# Add the custom CSS
demo.css = css

# Launch the interface
demo.launch()


