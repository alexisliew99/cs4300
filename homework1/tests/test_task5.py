# Implement pytest test cases to verify the correctness of 
# the code for each data structure.

from task5 import favorite_books, student_database

# check favourite 3 books return
def test_favorite_books():
    books, first_three = favorite_books()
    assert len(books) >= 3
    assert len(first_three) == 3
    assert first_three[0][0] == "The Night Circus" 
    assert first_three[1][0] == "Ready Player One"
    assert first_three[2][0] == "Badminton Basics"

# check the database matches student and id
def test_student_dictionary():
    db = student_database()
    assert db["Nick"] == 101
    assert "Yoyo" in db