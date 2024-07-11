# Gradio Project

This project demonstrates the use of Gradio interfaces for text generation and sentiment analysis using Hugging Face transformers. The project is organized into three files:

1. **sentiment-analysis.py**: Contains the sentiment analysis example.
2. **text-generation.py**: Contains the text generation example.
3. **combined.py**: Combines both examples into a single interface with tabs.

## Dependencies

Make sure you have the following dependencies installed:
- Python 3.7+
- Gradio
- transformers

You can install the necessary dependencies using pip:

```bash
pip install gradio transformers
```

# Running the Examples

To run the examples in this Gradio project, follow these steps:

1. **Sentiment Analysis Example**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you've saved the `sentiment-analysis.py` file.
   - Run the following command:
     ```bash
     python sentiment-analysis.py
     ```
   - The Gradio interface for sentiment analysis will launch in your browser.

2. **Text Generation Example**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you've saved the `text-generation.py` file.
   - Run the following command:
     ```bash
     python text-generation.py
     ```
   - The Gradio interface for text generation will launch in your browser.

3. **Combined Example**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you've saved the `combined.py` file.
   - Run the following command:
     ```bash
     python combined.py
     ```
   - The combined Gradio interface with tabs for both text generation and sentiment analysis will launch in your browser.

# File Descriptions

## `sentiment-analysis.py`
This file sets up a Gradio interface for sentiment analysis. It uses the Hugging Face transformers pipeline function to load a sentiment analysis model and defines a function `analyze_sentiment` to process the input text and return the sentiment label.

## `text-generation.py`
This file sets up a Gradio interface for text generation. It uses the Hugging Face transformers pipeline function to load a GPT-2 model for text generation and defines a function `generate_text` to generate text based on the input prompt.

## `combined.py`
This file sets up a combined Gradio interface with two tabs: one for text generation and one for sentiment analysis. It creates individual interfaces for each functionality and then combines them using the `gr.TabbedInterface`.

Feel free to explore and interact with these examples! 😊



