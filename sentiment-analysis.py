import gradio as gr
from transformers import pipeline

classifier = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    result = classifier(text)
    return result[0]['label']

gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text").launch(share=True)
