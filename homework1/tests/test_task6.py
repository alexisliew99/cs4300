# Pytest to verify word count from task6_read_me.txt with expected number.  
import os
import pytest
from task6 import count_words_in_file

@pytest.mark.parametrize("filename, expected", [
    # Absolute path to task6_read_me.txt
    # 127 is the expected numebr of word in the text file
    (
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "task6_read_me.txt")),
        127
    ),
])
def test_count_words_in_files(filename, expected):
    assert count_words_in_file(filename) == expected

# verify that an empty files returns a word count of 0 
# tmp_path to create a temp file for testing edge-case input.
def test_count_words_in_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")

    assert count_words_in_file(str(empty_file)) == 0


# test files with single-line content to make sure it is correct word count
@pytest.mark.parametrize("content, expected", [
    ("hello world", 2),
    ("one two three four", 4),
])
def test_count_words_in_small_files(tmp_path, content, expected):
    file = tmp_path / "sample.txt"
    file.write_text(content)

    assert count_words_in_file(str(file)) == expected