def rotate_matrix(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i]=matrix[i][::-1]

    return matrix

print("Enter the elements of the matrix : ")
matrix=[]
while True:
    row = input()
    if not row:
        break
    matrix.append([int(num) for num in row.split()])

output=rotate_matrix(matrix)

for row in output:
    print(' '.join(str(num) for num in row))
