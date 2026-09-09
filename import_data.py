import csv
from app import app, db, Review
from datetime import datetime
from textblob import TextBlob

with open("reviews.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    with app.app_context():
        for row in reader:
            blob = TextBlob(row["review_text"])
            polarity = blob.sentiment.polarity

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            review = Review(
                reviewer_name=row["reviewer_name"],
                review_text=row["review_text"],
                rating=int(row["rating"]),
                date_posted=datetime.strptime(row["date_posted"], "%Y-%m-%d").date(),
                sentiment=sentiment
            )
            db.session.add(review)

        db.session.commit()
        
