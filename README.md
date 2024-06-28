# Quorum's Python Test

## How to run it:
- To run the solution, just run ```python main.py``` in the project root.
- To run the tests, run ```python -m unittest test/quorum_test.py``` also in the project root.

## 1) Time complexity:

* [The longer the lists, the longer it takes](https://en.wikipedia.org/wiki/Big_O_notation)
* Tradeoffs: For a matter of simplicity, typed lists where used. Switching to ```Set()``` would be a way to improve performance since _sets_ are implemented as hashtables and have more efficient lookup. Specific algorithms (i.e binary search) can also be used to improve performance of this type of problem.

## 2) Future extension
* The solution was written in a way to abstract the fields as much as possible. the functions to read and write data, for instance, are not depending on any implementation. I used dataclasses, but using dictionaries maybe would allow even more customization.

## 3) Different Data Format
* The functions were implemented receiving lists as parameters. Other functions, for data conversion, were written in order to make the switching of sources easier. Similar mapping functions could be used for other sources of data with different formats.

## 4) Time spent on assignement
* The total time writting code: ~3h. It took me a while to organize things since I've been working exclusively with the Dart language in the past 2 months and I don't have any contact with Python since January.
