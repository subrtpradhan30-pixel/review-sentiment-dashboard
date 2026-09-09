import csv
from datetime import datetime
from textblob import TextBlob
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reviews.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewer_name = db.Column(db.String(1000), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.Date, nullable=False)
    sentiment = db.Column(db.String(20), nullable=True)


@app.route("/")
def home():
    sentiment_filter = request.args.get("sentiment", "All")

    all_reviews = Review.query.all()

    if sentiment_filter == "All":
        reviews = all_reviews
    else:
        reviews = Review.query.filter_by(sentiment=sentiment_filter).all()

    if all_reviews:
        average_rating = sum(review.rating for review in all_reviews) / len(all_reviews)
    else:
        average_rating = 0

    positive = 0
    negative = 0
    neutral = 0

    for review in all_reviews:
        if review.sentiment == "Positive":
            positive += 1
        elif review.sentiment == "Negative":
            negative += 1
        elif review.sentiment == "Neutral":
            neutral += 1

    rating_counts = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0
        }

    for review in all_reviews:
        if review.rating in rating_counts:
         rating_counts[review.rating] += 1

    total_reviews = len(all_reviews)


    if total_reviews > 0:
        positive_percent = (positive / total_reviews) * 100
        negative_percent = (negative / total_reviews) * 100
        neutral_percent = (neutral / total_reviews) * 100
    else:
        positive_percent = 0
        negative_percent = 0
        neutral_percent = 0

    return render_template(
        "dashboard.html",
        reviews=reviews,
        positive=positive,
        negative=negative,
        neutral=neutral,
        rating_counts=rating_counts,
        average_rating=average_rating,
        sentiment_filter=sentiment_filter,
        positive_percent=positive_percent,
        negative_percent=negative_percent,
        neutral_percent=neutral_percent,
    )
def seed_database():
    if Review.query.count() == 0:
        with open("reviews.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                analysis = TextBlob(row["review_text"])
                polarity = analysis.sentiment.polarity

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
                    date_posted=datetime.strptime(
                        row["date_posted"], "%Y-%m-%d"
                    ).date(),
                    sentiment=sentiment
                )

                db.session.add(review)

            db.session.commit()


with app.app_context():
    db.create_all()
    seed_database()

if __name__ == "__main__":
    app.run(debug=True)
