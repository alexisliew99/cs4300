# Create a new file named task5.py and inside create a list of your favorite books, including book
# titles and authors. Use list slicing to print the first three books in the list. Create a dictionary that
# represents a basic student database, including student names and their corresponding student IDs.

# list of fav books
def favorite_books():
    books = [
        ("The Night Circus", "Erin Morgenstern"),
        ("Ready Player One", "Ernest Cline"),
        ("Badminton Basics", "Sharon Baker"),
    ]
    return books, books[:3]

def student_database():
    return {"Nick": 101, "Yoyo": 102, "Steven": 103}
