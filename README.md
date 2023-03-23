# Pairwise Alignment Algorithms

1) Global Alignment - Needleman wunsch algorithm
   This is a dynamic programming algorithm used to align two sequences of nucleotides
   The code file 1 aligns the two sequences based upon the scoring scheme:-
   Match : +2
   Mismatch : -3
   Gap : -1
   
   Code file 2 aligns with scheme:-
   
   Match: +2
   Mismatch : -1
   Gap : -3
   
   and tries to see what happens on penalising the gaps more than mismatch on alignment

2) Local Alignment - Smith-Waterman Algorithm
   This is also a dynamic programming alogorithm that is used to align two sequences but now
   we are not penalising the gaps towards the ends and hence the alignment is done in a way that
   one sequence aligns with a subsequence of the other
