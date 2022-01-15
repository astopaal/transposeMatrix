#bu uygulama bir matrisin devriğini döngü ve list comprehension ile oluşturur
#this app creates transpose matrix using for loop and list comprehension

matrix = []

rows = int(input("how many rows do you want to create a matrix?\n"))

print("enter matrix rows with commas between elements \nGo to the next row by pressing enter after each row")

for i in range(rows):

    row = list(map(int, input().split(",")))
    matrix.append(row)

#comprehension

def usingComprehension(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

#for loop

def transposeUsingForLoop():
    transposeUsingForLoop = []

    for i in range(0, len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        transposeUsingForLoop.append(temp)

    return transposeUsingForLoop
    