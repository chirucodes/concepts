Author: Chiru Toleti
Dat: 20 Aug 2018
-------------------------------------------------------
Problem Statement :
-In the software language of your choice, and given standard algebraic notation of a chess board (see below), write code that will:

Accept two parameters:
-Type of chess piece (Queen, Rook, Knight)
-Current position on a chess board (for example: d2)

Return:
-A list of all the potential board positions the given piece could advance to, with one move, from the given position, with the assumption there are
no other pieces on the board.

Rules:
-You do not have to implement the solution for every piece type, but the solution must implement at least the following: Queen, Rook and
Knight.
-You may not use any external/non-core libraries: use only primitives and built-ins for the chosen language.
-Please provide test coverage for your work.

Example:
If the code is passed: “knight, d2”
$ chessercise.py -piece KNIGHT -position d2
The output should be: “b1, f1, b3, f3,c4, e4"

Algebraic Notation Legend:

---------------------------------------------------------
File tree:
.
├── ReadMe.txt
├── chessercise.py
└── piece_properties.json

chessercise.py: is a python module to solve the above problem statement.
piece_properties.json: is the default json file which contains properties of chess pieces.
-------------------------------------------------------
Assumptions:

I given names to directions as below.
m -> Towards Right
n -> Towards Left
o -> Towards Forward
p -> Towards Backward
q -> Towards diagonal between Right and Forward
r -> Towards diagonal between Left and Backward
s -> Towards diagonal between Forward and Left
t -> Towards diagonal between Backward and Right



      s     o      q
       \    |    /
        \   |   /
         \  |  /
          \ | /
           \|/
n<--------PIECE-------->m
           /|\
          / | \
         /  |  \
        /   |   \
       /    |    \
      r     p     t

And defined the steps as below.

Unidirectional directions: Rook, Queen
Added an integer/X before the direction character to define the position number the piece should get moved to.
Examples are mentioned below.
Unidirectional:
1m -> 1 step towards right from the current position.
2m -> 2nd step towards right from the current position.
nm -> nth step towards right from the current position.
Xm -> from the current position and upto the max number it can go to.
For eg: if the current position of the rook is f1, and the step is Xm then the posible positions are g1, h1

1n -> 1 step towards left from the current position.
2n -> 1 step towards left from the current position.
nn -> nth step towards left from the current position.
Xn -> from the current position and upto the max number it can go to.
For eg: if the current position of the rook is f1, and the step is Xm then the posible positions are a1, b1, c1, d1, e1

The same repeats for directions o,p,q,r,s and t

Bilateral directions: Knight
2m-1o => 2m -> 2nd step towards right from the current position and 1o ->  1 step towards forward from the temp position.
2m-1p => 2m -> 2nd step towards right from the current position and 1p ->  1 step towards Backward from the temp position.
2n-1o => 2n -> 2nd step towards left from the current position and 1o ->  1 step towards forward from the temp position.
2n-1p => 2n -> 2nd step towards left from the current position and 1p ->  1 step towards Backward from the temp position.
2o-1m => 2o -> 2nd step towards forward from the current position and 1m ->  1 step towards right from the temp position.
2o-1n => 2o -> 2nd step towards forward from the current position and 1n ->  1 step towards left from the temp position.
2p-1m => 2p -> 2nd step towards Backward from the current position and 1m ->  1 step towards right from the temp position.
2p-1n => 2p -> 2nd step towards Backward from the current position and 1n ->  1 step towards left from the temp position.

-------------------------------------------------------
python2.7 has been installed on the running machine and the python modules have been installed already.
----json
----optparse
-------------------------------------------------------

Known enhancements:
1) Can write logice for the remaining chess pieces aswell with the same logic, but with defined steps for pieces in json files.
2) Can add logging with a fixed format.
-------------------------------------------------------


Execution:
############################
$ python chessercise.py -h
Found piece_properties.json file
Object has been created successfully
Usage: python chessercise.py --piece=rook --position=a1

Options:
  -h, --help            show this help message and exit
  -i PIECE, --piece=PIECE
                        Name of the chess piece. Ex: rook
  -o POSITION, --position=POSITION
                        A json file which contains properties of chess pieces.
                        Ex: d4
$

############################
$ python chessercise.py --piece=rook --position=d4
Found piece_properties.json file
Object has been created successfully
rook is at position d4
Found steps in properties file for piece rook
A step (Xm) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xm
A step (Xn) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xn
A step (Xo) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xo
A step (Xp) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advanceable positions after processing the board is:  ['g4', 'f4', 'd1', 'h4', 'b4', 'a4', 'd8', 'd7', 'd6', 'e4', 'd5', 'd2', 'd3', 'c4']
$


############################
$ python chessercise.py --piece=knight --position=d4
Found piece_properties.json file
Object has been created successfully
knight is at position d4
Found steps in properties file for piece knight
A step (2m-1o) found in properties file, which is Bilateral
A step (2m-1p) found in properties file, which is Bilateral
A step (2n-1o) found in properties file, which is Bilateral
A step (2n-1p) found in properties file, which is Bilateral
A step (2o-1m) found in properties file, which is Bilateral
A step (2o-1n) found in properties file, which is Bilateral
A step (2p-1m) found in properties file, which is Bilateral
A step (2p-1n) found in properties file, which is Bilateral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advanceable positions after processing the board is:  ['f3', 'f5', 'b5', 'b3', 'c2', 'e6', 'c6', 'e2']
$



############################
$ python chessercise.py --piece=queen --position=d4
Found piece_properties.json file
Object has been created successfully
queen is at position d4
Found steps in properties file for piece queen
A step (Xm) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xm
A step (Xn) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xn
A step (Xo) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xo
A step (Xp) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xp
A step (Xq) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xq
A step (Xr) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xr
A step (Xs) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xs
A step (Xt) found in properties file, which is not empty and Unidirectional
Is starting with X
STEP:  Xt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advanceable positions after processing the board is:  ['h8', 'f4', 'd8', 'f6', 'f2', 'h4', 'b4', 'e5', 'b6', 'b2', 'd6', 'd7', 'd5', 'd2', 'd3', 'd1', 'e3', 'g7', 'g4', 'g1', 'a1', 'a4', 'a7', 'c3', 'e4', 'c5', 'c4']
$



