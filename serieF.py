print("Hecho por Alisson Dimas Arevalo\ny Arely Rivera Olivares")
limite=int(input("Ingrese el limite de la serie Fibonacci: "))
a,b=0,1
print(f"Números de Fibonacci hasta {limite}: ")
while a<= limite:
 print(f"{a}")
 a,b=b,a+b