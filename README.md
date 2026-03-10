# Email Spam Detection using NLP and Machine Learning

## Project Overview
This project focuses on building a machine learning model that can classify messages as spam or not spam. Spam messages are unwanted messages that often contain advertisements, scams, or misleading information. The goal of this project is to use Natural Language Processing (NLP) techniques to analyze message content and detect spam automatically.

## Objective
The main objective of this project is to understand and implement the complete machine learning workflow for text classification. The project demonstrates how raw text data can be processed, converted into numerical features, and used to train machine learning models for classification tasks.

## Technologies Used
- Python
- Pandas
- NumPy
- NLTK (Natural Language Processing)
- Scikit-learn
- Streamlit

## Methodology
The project follows a structured machine learning pipeline:
1. Dataset loading and exploration
2. Text preprocessing (cleaning, tokenization, stopwords removal)
3. Feature extraction using TF-IDF
4. Model training using machine learning algorithms
5. Model evaluation using performance metrics

## Features
- Detects spam messages
- Machine learning model trained on SMS dataset
- Simple web interface

## Expected Outcome
The final model will classify messages as spam or non-spam with good accuracy by learning patterns from the training dataset.

## Learning Outcome
Through this project, the aim is to gain practical understanding of NLP preprocessing, feature engineering, machine learning model training, and evaluation techniques used in text classification problems.

## How to Run

1. Install dependencies

pip install pandas scikit-learn streamlit

2. Run the app

cd notebooks
streamlit run app.py

## Example

Input:
Congratulations! You won a free iPhone

Output:
SPAM MESSAGE
