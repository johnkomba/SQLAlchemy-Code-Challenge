# app/main.py
from app.models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Restaurant
from app.models import Customer
from app.models import Review

engine = create_engine('sqlite:///restaurant_reviews.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example application logic
def display_reviews():
    reviews = session.query(Review).all()
    for review in reviews:
        print(f"Review for {review.restaurant.name} by {review.customer.first_name} {review.customer.last_name}: {review.star_rating} stars.")

if __name__ == "__main__":
    display_reviews()
