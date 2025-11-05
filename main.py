from random import randint


# matriz=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]


# print(matriz[1][1])

# n=4
# matriz =[]

# for i in range(n):
#     fila = []
#     for j in range(n):
#         fila.append(int(input(f"inserte el valor numero{j}: ")))
#     matriz.append(fila)

# for i in range(n):
#     print("{", end=" ")
#     for j in range(0,n):
#         print(f"{matriz[i][j]}, ",end=" ")
#     print("}", end=" ")
#     print("")

def crearMatriz(n):
    matriz=[]

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(randint(0,10))
        matriz.append(fila)
    return matriz

def sumarMatriz(A,B):
    matriz=[]
    
    for i in range(len(A)):
        fila = []
        for j in range(len(A)):
            fila.append(A[i][j] + B[i][j])
        matriz.append(fila)

    return matriz

A = crearMatriz(2)
print(A)
B = crearMatriz(2)
print(B)
print (sumarMatriz(A,B))


def multiplicarMatriz(A,B):
    matriz=[]
    
    for i in range(len(A)):
        fila = []
        for j in range(len(A)):
            val = 0
            for k in range(len(A)):
                val += A[i][k] * B[k][j]
            fila.append(val)    
        matriz.append(fila)
    return matriz

print (multiplicarMatriz(A,B))