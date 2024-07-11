import gradio as gr
from transformers import pipeline

# Load the text generation pipeline with a specific model
generator = pipeline('text-generation', model='gpt2')

# Function for text generation
def generate_text(prompt):
    result = generator(prompt, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']

# Load the sentiment analysis pipeline
classifier = pipeline('sentiment-analysis')

# Function for sentiment analysis
def analyze_sentiment(text):
    result = classifier(text)
    return result[0]['label']

# Create the text generation interface
text_gen_interface = gr.Interface(fn=generate_text, inputs="text", outputs="text")

# Create the sentiment analysis interface
sentiment_interface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")

# Create a tabbed interface to combine both
tabbed_interface = gr.TabbedInterface([text_gen_interface, sentiment_interface], ["Text Generation", "Sentiment Analysis"])

# Launch the tabbed interface
tabbed_interface.launch(share=True)
