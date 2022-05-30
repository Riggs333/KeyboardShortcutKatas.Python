# Expand/Extend Selection

Place the cursor somewhere in the block of code you want to extract as a function or variable.

Use

* 'expand selection' (VS Code)
* 'extend selection' (PyCharm)

Lookup the keyboard shortcut for your tool.

## Refactor [tennis_game1.py](tennis_game1.py)

Use expand selection to select the piece of code shown in each sample below, then use 'extract method' or 'extract variable' or 'extract constant' with the name given.
Do not use the mouse!

Keep these instructions at the side of the window somewhere.
Run the test in [tennis_test.py](tennis_test.py) after each refactoring.

## Extract variable
Find the following snippet and extract it to a new local variable named `is_tie`.
```python
self.p1points == self.p2points
```

## Extract method/function
Find the following snippet and extract it to a new function `score_when_tied`.
```python
{
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
}.get(self.p1points, "Deuce")
```


## Extract constant (PyCharm only) 
Find the following snippet and extract it to a new constant `ALL`.
```python
"All"
```

Find the following snippet and extract it to a new constant `SEPARATOR`.
```python
"-"
```

## Extract function
Find the following snippet and extract it to a new function `is_advantage_or_win`.
```python
self.p1points >= 4 or self.p2points >= 4
```

## Extract function
Find the following snippet and extract it to a new function `score_name`.
```python
{
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}[temp_score]
```

## Bonus: Use your imagination

Extract any more functions, constants, variables or fields that you want to. Continue to use Expand Selection and don't use the mouse!
