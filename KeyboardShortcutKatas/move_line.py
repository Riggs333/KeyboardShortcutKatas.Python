""" Move Line
Sort the append statements below to make the test pass
using only move line up/down (you can move multiple lines at a time)
Lookup the keyboard shortcuts for your tool!
"""

numbers_as_words = []
numbers_as_words.append("three")
numbers_as_words.append("five")
numbers_as_words.append("nine")
numbers_as_words.append("two")
numbers_as_words.append("ten")
numbers_as_words.append("six")
numbers_as_words.append("seven")
numbers_as_words.append("one")
numbers_as_words.append("four")
numbers_as_words.append("eight")


def test_numbers_in_order():
    assert numbers_as_words == [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]


"""
Also, sort the test cases below alphabetically.
If you put the cursor on the test name, you should be able to move the whole 
test case up and down in the same way as you can move single lines of code.

Bonus points if you jump from method to method using a shortcut ;-)
"""


def test_omega():
    assert "o" == "o ".strip()


def test_epsilon():
    assert "e" == "  e  ".strip()


def test_beta():
    assert "b" == " b".strip()


def test_alpha():
    assert "a" == " a ".strip()


def test_gamma():
    assert "g" == " g ".strip()
