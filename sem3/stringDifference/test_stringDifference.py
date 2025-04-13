import pytest
from stringDifference import stringDifference

@pytest.mark.parametrize("a, b, expected", [
    # Basic test cases
    ("abc", "abcd", "d"),
    ("hello", "hellox", "x"),
    ("test", "ttese", "e"),
    
    # Empty string test case
    ("", "a", "a"),
    
    # Single character test case
    ("a", "aa", "a"),
    
    # Test case with numbers
    ("123", "1234", "4"),
    
    # Test case with special characters
    ("a!b", "!ab#", "#"),
    
    # Test with repeated characters
    ("aab", "aaba", "a"),
    
    # Test with spaces
    ("hello world", "hello worlds", "s"),
    
    # Test with uppercase and lowercase
    ("aBc", "aBcD", "D"),
    
    # Test with more complex shuffling
    ("algorithm", "logarithma", "a"),
    
    # Test with different types of characters
    ("a1b2", "1a2b!", "!"),
])
def test_stringDifference(a, b, expected):
    assert stringDifference(a, b) == expected