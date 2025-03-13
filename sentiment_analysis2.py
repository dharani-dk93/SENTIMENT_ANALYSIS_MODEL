import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER model if not already installed
nltk.download('vader_lexicon')

# Initialize Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiments(sentences):
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    for sentence in sentences:
        score = sia.polarity_scores(sentence)

        if score['compound'] >= 0.05:
            positive_count += 1
        elif score['compound'] <= -0.05:
            negative_count += 1
        else:
            neutral_count += 1

    return {
        "Positive Statements": positive_count,
        "Negative Statements": negative_count,
        "Neutral Statements": neutral_count
    }

# Get user input
print("Enter your sentences (type 'END' to finish):")
user_sentences = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    user_sentences.append(line)

# Analyze sentiment
result = analyze_sentiments(user_sentences)
print("\nSentiment Analysis Result:")
print(result)
