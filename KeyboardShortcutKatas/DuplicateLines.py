"""
Duplicate Lines and Delete Lines

Instead of copying and pasting code with two separate keyboard shortcuts,
you can also duplicate one or more lines.
This is often convenient for example when creating parameterized tests.

You can also delete the whole line of the current cursor position.

Fix and add missing test cases below by catching all cases between 0 and 10
using shortcuts for Duplicate and Delete Line.

Duplicate line is also called "Copy Line Up/Down" in VS Code
"""
import pytest


@pytest.mark.parametrize("number, expected_square", [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 5),
    (3, 9),
    (4, 16),
    (6, 36),
    (7, 49),
    (9, 81)
])
def test_squares(number, expected_square):
    assert number * number == expected_square
