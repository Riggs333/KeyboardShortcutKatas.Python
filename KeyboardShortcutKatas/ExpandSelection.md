# Expand/Extend Selection

Place the cursor somewhere in the block of code you want to extract as a function or variable.
Use
* 'expand selection' (VS Code)
* 'extend selection' (PyCharm)
Lookup the keyboard shortcut for your tool

## Refactor Tennis1.py
Use expand selection to select the piece of code shown in each sample below, then use 'extract method' or 'extract variable' or 
'extract constant' with the name given.
Do not use the mouse!

Keep these instructions at the side of the window somewhere.
Run the test in TennisTest.py after each refactoring.

## Extract variable
<pre> 
self.p1points == self.p2points
</pre>
Extract to local variable named `is_tie`.

## Extract method/function
<pre>
{
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
}.get(self.p1points, "Deuce")
</pre>
Extract to function `score_when_tied`.

## Extract constant (PyCharm only) 
<pre>
"All"
</pre>
Extract to constant `ALL`.

<pre>
"-"
</pre>
Extract to constant `SEPARATOR`.

## Extract function
<pre>
self.p1points >= 4 or self.p2points >= 4
</pre>
Extract to function `is_advantage_or_win`.

## Extract function
<pre>
{
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}[temp_score]
</pre>
Extract to function `score_name`.

## Use your imagination
Extract any more functions, constants, variables or fields that you want to. Continue to use Expand Selection and don't use the mouse!
