import random


def get_generation(matrix, n):
   
    result = [[0] * len(row) for row in matrix]
    for _ in range (n):
       
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                alive = 0


                for row in range((i-1), i+2):
                    for column in range(j-1, j +2):
                        alive+=matrix[row%len(matrix)][column%len(matrix[i])]
                alive -= matrix[i][j]
                if alive == 3:
                    result[i][j] = 1
                elif alive ==2:
                    result[i][j] = matrix[i][j]
                elif alive < 2:
                    result[i][j] = 0
                else:
                    result[i][j] = 0
        matrix = [row[:] for row in result]
    
    
    return matrix

matrix = [[random.randint(0, 1) for _ in range(20)] for _ in range(20)]

matrix = get_generation(matrix, 20)





    
    
    
    




