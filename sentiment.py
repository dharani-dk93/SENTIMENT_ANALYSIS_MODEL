from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def analyze_sentiments(sentences):
    positive = negative = neutral = 0

    for sentence in sentences:
        score = sia.polarity_scores(sentence)

        if score['compound'] >= 0.05:
            positive += 1
        elif score['compound'] <= -0.05:
            negative += 1
        else:
            neutral += 1

    total = positive + negative + neutral
    rating = round((positive * 5 + neutral * 3) / total, 1) if total else 0

    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "rating": rating
    }
