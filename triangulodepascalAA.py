print ("Hecho por Alisson Dimas Arevalo\ny Arely Rivera Olivares")
print ("Programa del triangulo pascal")
def triangulo_de_pascal(n):
    triangulo = [[1]]
    for i in range(1, n):
        fila_anterior = triangulo[-1]
        nueva_fila = [1]  
        for j in range(1, len(fila_anterior)):
            suma = fila_anterior[j - 1] + fila_anterior[j]
            nueva_fila.append(suma) 
        nueva_fila.append(1)  
        triangulo.append(nueva_fila)
    return triangulo
n_filas = int(input("Introduce el número de filas para el Triángulo de Pascal: "))
triangulo = triangulo_de_pascal(n_filas)
for fila in triangulo:
    print(fila)
    