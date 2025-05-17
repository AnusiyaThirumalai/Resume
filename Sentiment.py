from textblob import TextBlob

def analyze_sentiment(review):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

if _name_ == "_main_":
    print("Product Review Sentiment Analyzer")
    while True:
        review = input("\nEnter your product review (or type 'exit' to quit):\n> ")
        if review.lower() == 'exit':
            print("Goodbye!")
            break

        sentiment = analyze_sentiment(review)
        print(f"Sentiment: {sentiment}")
