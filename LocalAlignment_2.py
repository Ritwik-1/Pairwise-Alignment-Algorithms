# l1 = [A,T,T,A,C]
# l2 = [A,T,G,C]
# matrix : l3 : len(l1)+1 vs len(l2)+1
# col : l1
# row : l2

gap = -3
mismatch = -1
match = 2

ans = ["",""]

def printMatrix(matrix,s1_col,s2_row):
    for i in range(len(s2_row)+1):
        for j in range(len(s1_col)+1):
            print(matrix[i][j],end = " ")
        print("\n")

# diagonal ke liye call maro agar i==0 and j==0 
def FindPossibleWays(matrix,s1_col,s2_row,i,j):
    global ans
    if i < 0  or j < 0:
        return
    elif matrix[i][j] == 0:
        ans[0] = ans[0][::-1]
        ans[1] = ans[1][::-1]
        print("Possible Solution :-")
        print(ans[0])
        print(ans[1])
        return
    else:
        initial_ans1 = ans[0]
        initial_ans2 = ans[1]
        if(s1_col[j-1] == s2_row[i-1] and (matrix[i-1][j-1] + match == matrix[i][j])):
            ans[0]+=s2_row[i-1]
            ans[1]+=s1_col[j-1]
            FindPossibleWays(matrix,s1_col,s2_row,i-1,j-1)
            ans[0] = initial_ans1
            ans[1] = initial_ans2
        if(s1_col[j-1] != s2_row[i-1] and (matrix[i-1][j-1] +mismatch == matrix[i][j])):
            ans[0]+=s2_row[i-1]
            ans[1]+=s1_col[j-1]
            FindPossibleWays(matrix,s1_col,s2_row,i-1,j-1)
            ans[0] = initial_ans1
            ans[1] = initial_ans2
        if matrix[i-1][j] + gap == matrix[i][j]:
            ans[1]+= "_"
            ans[0]+= s2_row[i-1]                 
            FindPossibleWays(matrix,s1_col,s2_row,i-1,j)
            ans[0] = initial_ans1
            ans[1] = initial_ans2
        if matrix[i][j-1] +gap == matrix[i][j]:
            ans[0]+= "_"
            ans[1]+= s1_col[j-1]
            FindPossibleWays(matrix,s1_col,s2_row,i,j-1)
            ans[0] = initial_ans1
            ans[1] = initial_ans2

def GlobalAlignScore(matrix,s1_col,s2_row):

    for i in range(len(s2_row)+1):
        if(i == 0):
            for j in range(len(s1_col)+1):
                matrix[0][j] = 0
        else:
            matrix[i][0] = 0

    for i in range(1,len(s2_row)+1):
        for j in range(1,len(s1_col)+1):
            gap_score_1 = matrix[i][j-1] + gap
            gap_score_2 = matrix[i-1][j] + gap
            match_score = 0
            mis_match_score = 0
            if(s1_col[j-1] == s2_row[i-1]):
                    match_score = matrix[i-1][j-1] + match
                    max_4_val = max(gap_score_1,gap_score_2,match_score)
                    if(max_4_val < 0 ):
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = max_4_val
            else:
                mis_match_score = matrix[i-1][j-1] + mismatch
                max_4_val = max(gap_score_1,gap_score_2,mis_match_score)
                if(max_4_val < 0 ):
                        matrix[i][j] = 0
                else:
                        matrix[i][j] = max_4_val
    
    printMatrix(matrix,s1_col,s2_row)

    max_i = 0
    max_j = 0

    for i in range(len(s2_row)+1):
        for j in range(len(s1_col)+1):
            if(matrix[i][j] > matrix[max_i][max_j]):
                max_i = i
                max_j = j

    return matrix[max_i][max_j]


s1_col = input("Enter first sequence : ")
s2_row = input("Enter second sequence :")
matrix = []

for i in range(len(s2_row)+1):
    column = []
    for j in range(len(s1_col)+1):
        column.append(0)
    matrix.append(column)

score = GlobalAlignScore(matrix,s1_col,s2_row)

print("The alignment score is : ",score)

max_i = 0
max_j = 0

for i in range(len(s2_row)+1):
    for j in range(len(s1_col)+1):
        if(matrix[i][j] > matrix[max_i][max_j]):
            max_i = i
            max_j = j

FindPossibleWays(matrix,s1_col,s2_row,max_i,max_j)


