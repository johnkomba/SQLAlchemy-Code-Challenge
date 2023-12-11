#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Customer,Restaurant,Review,Base

if __name__ == '__main__':
    fake = Faker()

    engine = create_engine('sqlite:///restaurants.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Review).delete()
    session.query(Restaurant).delete()
    session.query(Customer).delete()

    # Create Restaurants
    restaurants = []
    for _ in range(10):
        restaurant = Restaurant(
            name=fake.company(),
            price=random.randint(1, 5)
        )
        session.add(restaurant)
        restaurants.append(restaurant)
        session.commit()

              

    # Create Customers
    customers = []
    for _ in range(20):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(customer)
        customers.append(customer)

        session.commit()

    # Create Reviews
    reviews = []
    for _ in range(50):
        review = Review(
            star_rating=random.randint(1, 5),
            restaurant_id=random.choice(restaurants).id,
            customer_id=random.choice(customers).id,
           
        )
        session.add(review)
        reviews.append(review)

        session.commit()
    session.close()
