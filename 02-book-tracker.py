# Exercise 1: The Bookworm's Inventory

# Create the dictionary, "book", with key/value pairs as mentioned above
book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "on_shelf": False,
    "borrower": "Arthur Dent",
    "overdue": True,
    "on_hold": False
}


# Exercise 2: Is It On the Shelf?

# Create an if/else statement
if book['on_shelf'] == True and book['on_hold'] == False:

    # Print "Book is available to be borrowed"
    print("Book is available to be borrowed")

else:

    # Print "Book is not available to be borrowed"
    print("Book is not available to be borrowed")


# Exercise 3: On Hold or Overdue?

# Create an if/else statement
if book['overdue'] == True:

    # Print "Book is overdue - Contact <Borrower's name> to return it"
    print(f"Book is overdue - Contact {book['borrower']} to return it")

else:

    # Set "book['on_hold']" to "True"
    book['on_hold'] = True

    # Print "Book has been put on hold"
    print("Book has been put on hold")


# Exercise 4: Tracking Down the Borrower

# List of dictionaries with borrower contact information
borrowers_list = [
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@dlailibrary.com",
        "phone": "+1111111111"
    },
    {
        "name": "Bob Smith",
        "email": "bob.smith@dlailibrary.com",
        "phone": "+2222222222"
    },
    {
        "name": "Arthur Dent",
        "email": "arthur.dent@dlailibrary.com",
        "phone": "+3333333333"
    },
    {
        "name": "Diana Prince",
        "email": "diana.prince@dlailibrary.com",
        "phone": "+4444444444"
    }
]

# Iterate through the borrowers_list
for borrower in borrowers_list:

    # Check if the borrower names match
    if book['borrower'] == borrower['name']:

        # Store the email
        borrower_email = borrower['email']


# Print the information
print(f"{book['borrower']}'s email is: {borrower_email}")


# Exercise 5: The LLM to the Rescue!

# Name of the borrower
person_name = book['borrower']

# Name of the book
book_name = book['title']

# Name of book's author
book_author = book['author']

# Due Date
due_date = "16 November 2024"

# Create the prompt
prompt = f"""
Please write a polite email to {person_name}, reminding them to return the book "{book_name}" by {book_author}. The book was due on {due_date}.
"""

print(prompt)
