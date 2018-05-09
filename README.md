# Unwrap Text [Daily Programmer Challenge 359](https://www.reddit.com/r/dailyprogrammer/comments/8gjc3k/20180502_challenge_359_intermediate_unwrap_some/)

Assumes at least one line wraps, by choosing that line as the maximum length of a line. Then if the length of a line plus the length of the next word equal or exceed the max length it removes the line wrap.

## Input

Input consists of a single text file containing line breaks. It assumes that the longest line is where the word wrap occurs and will remove the line breaks from any line that it assumes is wrapped. 

The input as programmed is:
     
     demotext.txt

    
## Output 
Outputs the the text of the file into the stdout, without the word wrapping.
