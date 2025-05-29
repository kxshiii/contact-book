from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contact_book_orm.models.contact import Contact
from sqlalchemy.orm import declarative_base
Base = declarative_base()

engine = create_engine('sqlite:///contact_book.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_contact(first_name, last_name, email, phone, password_salt=None, password_hash=None):
    contact = Contact(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone,
        password_salt=password_salt,
        password_hash=password_hash
    )
    session.add(contact)
    session.commit()

def get_contacts():
    return session.query(Contact).all()

def find_contact_by_email(email):
    """Find a contact by email."""
    return session.query(Contact).filter_by(email=email).first()

if __name__ == "__main__":
    # Example: Add a contact (without password)
    add_contact("John", "Doe", "john.doe@example.com", "555-1234")
    # Example: List all contacts
    contacts = get_contacts()
    for c in contacts:
        print(f"{c.first_name} {c.last_name} - {c.email} - {c.phone}")

    # Example: Find a contact by email
    email_to_find = "john.doe@example.com"
    found = find_contact_by_email(email_to_find)
    if found:
        print(f"Found: {found.first_name} {found.last_name} - {found.email}")
    else:
        print(f"No contact found with email: {email_to_find}")
