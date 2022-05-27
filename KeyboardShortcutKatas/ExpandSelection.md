# Expand Selection

Place the cursor somewhere in the block of code you want to extract as a function.
Use 'expand selection' NOT THE MOUSE!
Lookup the keyboard shortcut for your tool, it's often Alt-⬆

## Refactor TennisGame1.py
Use expand selection to select the piece of code shown,
then use 'extract method' or 'extract variable' or 'extract constant'
with the name given.
Do not use the mouse!

Keep these instructions at the side of the window somewhere.
Run the test in TennisTest.py after each refactoring.

## is_tie
variable
<pre> 
self.p1points == self.p2points
</pre>


## score_when_tied
method
<pre>
result = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
}.get(self.p1points, "Deuce")
</pre>

## ALL 
constant
<pre>
"All"
</pre>

## Separator
constant
<pre>
"-"
</pre>

## is_advantage_or_win
method
<pre>
self.p1points >= 4 or self.p2points >= 4
</pre>

## score_name
method
<pre>
{
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}[temp_score]
</pre>

## Use your imagination
Extract any more functions, constants, variables or fields that you want to. Continue to use Expand Selection and don't use the mouse!
