import gradio as gr
from transformers import pipeline

# Load the text generation pipeline with a specific model
generator = pipeline('text-generation', model='gpt2')

# Function for text generation
def generate_text(prompt):
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']

# Create the Gradio interface
gr.Interface(fn=generate_text, inputs="text", outputs="text").launch(share=True)
