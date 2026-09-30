# Review Sentiment Dashboard

A Flask-based web application that analyzes customer reviews and presents sentiment and rating insights through an interactive dashboard.

## Features

- Import customer reviews from a CSV file
- Store reviews using SQLite and SQLAlchemy
- Analyze review sentiment using TextBlob
- Classify reviews as Positive, Negative, or Neutral
- Display sentiment percentages
- Calculate average rating
- Filter reviews by sentiment
- Visualize sentiment distribution using a pie chart
- Visualize rating distribution using a bar chart
- Responsive dashboard interface

## Tech Stack

- Python
- Flask
- SQLAlchemy
- SQLite
- TextBlob
- HTML
- CSS
- JavaScript
- Chart.js
- Gunicorn
- Render

## How It Works

1. Review data is stored in a CSV file.
2. The application reads the review data using Python.
3. TextBlob analyzes the review text and calculates sentiment polarity.
4. Reviews are classified as Positive, Negative, or Neutral.
5. The review data is stored in the SQLite database using SQLAlchemy.
6. Flask retrieves the data from the database.
7. Jinja templates display the data on the dashboard.
8. JavaScript and Chart.js create the visualizations.

## Project Structure

```text
project/
├── app.py
├── import_data.py
├── reviews.csv
├── requirements.txt
├── Procfile
├── .gitignore
├── templates/
│   └── dashboard.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── dashboard.js```
##Local Setup

Clone the repository
git clone https://github.com/subrtpradhan30-pixel/review-sentiment-dashboard.git

Create a virtual environment
python -m venv .venv

Install dependencies
pip install -r requirements.txt

Import the review data
python import_data.py

Run the Flask application
python app.py

Then open the local address shown by Flask in your browser.

Deployment
The application is deployed using Render with Gunicorn.

Dataset
The project currently uses 150 customer reviews containing reviewer information, review text, ratings, and dates.

Future Improvements
Improve sentiment analysis for nuanced reviews
Add more advanced analytics
Move from SQLite to PostgreSQL