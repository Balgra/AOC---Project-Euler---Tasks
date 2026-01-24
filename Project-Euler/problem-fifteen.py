# Using Lattice path

# How many paths are in a 20x20 grid

matrix = [[0]*21 for _ in range(21)]
matrix[20][20]=1

#I could have made the Column 20 and Row 20 1 at the beginning .  Something that could have been Refactored

for i in range(20,-1,-1):

    for j in range(20,-1,-1):

        if i == 20:
            if j == 20:
                pass
            else:
                matrix[i][j] = matrix[i][j+1]
        elif j == 20: 
            if i == 20:
                pass
            else:
                matrix[i][j] = matrix[i+1][j]
        else:
            matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]

print(matrix[0][0])
