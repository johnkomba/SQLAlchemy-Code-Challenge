
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Connect to the database
DATABASE_URL = "sqlite:///restaurants.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def test_models():
    # Create sample instances
    restaurant1 = Restaurant(name="Restaurant 1", price=20)
    restaurant2 = Restaurant(name="Restaurant 2", price=30)

    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Doe")

    # Add instances to the session
    session.add_all([restaurant1, restaurant2, customer1, customer2])
    session.commit()

    # Test the methods
    print("All Reviews for Restaurant 1:")
    print(restaurant1.all_reviews(session))

    print("\nFanciest Restaurant:")
    fanciest_restaurant = Restaurant.fanciest(session)
    print(f"{fanciest_restaurant.name} - Price: {fanciest_restaurant.price}")

    print("\nFull Name of Customer 1:")
    print(customer1.full_name())

    print("\nFavorite Restaurant for Customer 1:")
    favorite_restaurant = customer1.favorite_restaurant()
    print(favorite_restaurant.name if favorite_restaurant else "No favorite restaurant")

    print("\nAdding Review for Customer 1:")
    customer1.add_review(session, restaurant1, rating=5)
    print("All Reviews for Restaurant 1 after adding review:")
    print(restaurant1.all_reviews(session))

    print("\nDeleting Reviews for Customer 1 and Restaurant 1:")
    customer1.delete_reviews(session, restaurant1)
    print("All Reviews for Restaurant 1 after deleting reviews:")
    print(restaurant1.all_reviews(session))

# Run the test
test_models()

# Close the session
session.close()
