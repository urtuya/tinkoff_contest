# Anti-plagiarism utility | Python3
## Utility that compares two text of Python programs and gives an estimate of their similarity

## Usage:
```
compare.py [-h] input_file [output_file]
```
An anti-plagiarism utility that compares two texts of Python programs and gives an estimate of their similarity.

### Args:
  - input_file   - a file contains one or several pairs of paths to python programs.
  - output_file  - an optional argument, a file contains path to the file for saving results. Default path: scores.txt .

_________________
## Example
There is an example for the input file in the directory: _input.txt_

```
files/main.py plagiat1/main.py
files/lossy.py plagiat2/lossy.py
files/lossy.py files/lossy.py
```


The program calculates the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) for each pair of programs and save result to a new file called _scores.txt_ in the same directory.

An example of output file(by default is scores.txt) with results:
```
0.84765
0.30681
1.0
```
