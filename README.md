[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-8d59dc4de5201274e310e4c54b9627a8934c3b88527886e3b421487c677d23eb.svg)](https://classroom.github.com/a/wTIe0hZN)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10717520)
# string_pattern
## Problem Intraduction
In this problem, your goal is to implement the Rabin Karp's algorithm.

## Problem Description
**Task.** 
In this problem your goal is to implement the Rabin Karp's algoritm for searching given patter in given text.

**Input format.** 
Input choice I or F (for input from keyboard or from file, as there is only one test file, after F assume that you need to open the only test sample file).
After that there are two strings in the input: the pattern P and the text T.

**Constraints.**
1 <= | P | <= T <= 5 * 10^5
The toal lenght of all occurances of P in T doesn't exceed 10^8.
The pattern and the text contain only latin letters.
*Take notice of github keyboard input as displayed in autograding file.

**Output format.**
Print all the positions of the occurances of P in T in the ascending order. Use 0-based indexing of positions in the text T.


**although** not a checked requirement - if everything works correctly, algorithm should take less than 5 seconds.

## Samples
### Sample 1
**Input**
aba
abacaba
**Output**
0 4
**Explanation**
The pattern aba can be found in position 0 (**aba**caba) and 4 (abac**aba**).
### Sample 2
**Input**
Test
testTesttesT
**Output**
4
**Explanation**
Pattern and text are case-sensitive in this problem. Pattern Test can only be found in position 4.
### Sample 3###
**Input**
aaaaa
baaaaaaa
**Output**
1 2 3
**Explanation**
Note that the occurances of the pattern in thetext can be overlapping, and that's ok, you still need to output all of them.

### Hints
* Beware of integer overflow
* Beware of taking negative numbers
* Use == in python as it will work faster thay implementing a function for areEqual

### Notice
If program will work, but won't contain said algorithm - autograding points will be anulled.
