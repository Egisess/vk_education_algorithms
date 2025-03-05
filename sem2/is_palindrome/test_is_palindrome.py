import pytest
from is_palindrome import is_palindrome, is_palindrome_2

@pytest.mark.parametrize("string, expected", [
    ("racecar", True),
    ("madam", True),
    ("abba", True),
    ("a", True),
    ("", True),
    ("hello", False),
    ("world", False),
    ("A man a plan a canal Panama", False),
    ("No lemon, no melon", False),
    ("Was it a car or a cat I saw", False),
])
def test_is_palindrome(string, expected):
    assert is_palindrome(string) == expected
    assert is_palindrome_2(string) == expected
