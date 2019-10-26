# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

# Example:

# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]

# The clockwise spiral traversal of this array is:

# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

# Here is a starting point:

def matrix_spiral_print(M):
    fullLength = len(M) * len(M[0])
    count = -1
    finalArr = [M[0][0]]
    cycleComplete = False

    rowL , colL = len(M),len(M[0])
    row,col = 0,0
    rowTraverse = False
    r_rev = True
    c_rev = False
    c_low_limit = 0
    r_low_limit = 0
    r_limit = rowL - 1
    c_limit = colL - 1

    for index in range(1,fullLength):
        if rowTraverse:
            row = row - 1 if r_rev else row + 1
            if row == r_limit :
                
                c_rev = not c_rev
                row = rowL - 1
                rowTraverse = False
                # if row == r_low_limit:
                #     r_low_limit += 1
                # if row == r_upper_limit:
                #     r_upper_limit -= 1
                
        else:            
            col = col - 1 if c_rev else col + 1
            if col == c_limit :
                r_limit = r_limit  - 1
                
                r_rev = not r_rev
                
                
                rowTraverse = True
                # if col == c_low_limit:
                #     c_low_limit += 1
                # if col == c_upper_limit:
                #     c_upper_limit -= 1

        finalArr.append(M[row][col])
    return finalArr

        # 00 01 02 03 04 14 24 34 




    

  # Fill this in.

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]




grid1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

grid2 = [[1,  2,  3,  4,  5,6],
        [7,  8,  9,  10,11,12],
        [13, 14, 15,16,17,18],
        [19, 20,21,22,23,24]]



# 00 01 02 03 04 05 
# 15 25 35        


# 00 01 02 
# 12 22 
# 21 20 
# 10 11


# 00 01 02 03 04
# 14 24 34 
# 33 32 31 
# 30 20 10 
# 11 12 13 
# 23 22 21





print(matrix_spiral_print(grid))
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
