from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment

def main():
    text = input("Enter text for sentiment analysis: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
