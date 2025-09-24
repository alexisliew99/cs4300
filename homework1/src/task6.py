# This reads text file and counts the number of words 
# Open the text file and reads the contents and count the number of words it contains.

def count_words_in_file(filename):

    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()
    return len(words)