# Kyrus Enigma

Puzzles from Kyrus Tech:

https://www.kyrus-tech.com/enigma

## Puzzle 00

### Problem

Find a, b, c, d, e, f, and g, all positive integers greater than 1, that satisfy all equations:
```
a2 × b × c2 × g = 5100
a × b2 × e × f2 = 33462
a × c2 × d3 = 17150
a3 × b3 × c × d × e2 = 914760
```
in the fastest way possible, using your language of choice.

### Solution

Create a python script to automate the factorization and computation process: [puzzle00.py](puzzle00.py).

Run script:
```
$ python3 puzzle00.py 
Prime factorization of 5100: {2: 2, 3: 1, 5: 2, 17: 1}
Prime factorization of 33462: {2: 1, 3: 2, 11: 1, 13: 2}
Potential 'a' values: [2]
Potential 'b' values: [3]
Prime factorization of 17150: {2: 1, 5: 2, 7: 3}
Prime factorization of 914760: {2: 3, 3: 3, 5: 1, 7: 1, 11: 2}
a: 2, b: 3, c: 5, d: 7, e: 11, f: 13, g: 17
Equation1: 5100
Equation2: 33462
Equation3: 17150
Equation4: 914760
```

## Puzzle 01

### Problem

Download and solve the puzzle below.

[puzzle.txt](puzzle.txt)

### Solution

The [puzzle.txt](puzzle.txt) file contains hashes. The first five hashes can be reversed with a site like hashtoolkit.com. 

```
d41d8cd98f00b204e9800998ecf8427e [Empty string]
61e9c06ea9a85a5088a499df6458d276 W
0cde1252d73b5bb4352e9287f281cca4 Wh
4ee972120bcda675f75222c87cb9d356 Who
ced02f3c3e78f15aec5d89bd71712cb0 Who 
```

Automate this process with a python script ([puzzle01.py](puzzle01.py)) to reverse as many hashes as possible. 