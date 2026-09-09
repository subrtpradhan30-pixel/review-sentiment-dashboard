from textblob import TextBlob

texts = [
    "I love this product!",
    "I hate this product!",
    "This product is okay.",
    "The product is absolutely fantastic!",
    "The product is terrible."
]

for text in texts:
    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(text)
    print("Polarity:", polarity)
    print("Sentiment:", sentiment)
    print()