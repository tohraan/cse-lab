from cselab.is_palindrome import is_palindrome


def test_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("")
    assert is_palindrome(" ")
    assert not is_palindrome("race a car")
