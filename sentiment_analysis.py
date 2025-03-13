import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER model
nltk.download('vader_lexicon')

# Initialize Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiments(sentences):
    positive_count = 0
    negative_count = 0

    for sentence in sentences:
        score = sia.polarity_scores(sentence)

        # Classify based on compound score
        if score['compound'] >= 0.05:
            positive_count += 1
        elif score['compound'] <= -0.05:
            negative_count += 1

    return {"Positive Statements": positive_count, "Negative Statements": negative_count}

# Example Input
sentences = [
    "I love this product, it's amazing!",
    "The weather is terrible today.",
    "I'm feeling great and excited!",
    "This is the worst experience I've ever had.",
    "It's an average day, nothing special."
]

# Get sentiment analysis results
result = analyze_sentiments(sentences)
print(result)
