lista_de_primos = []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if  n % i == 0:
            return False
    return True         

for i in range(101):
    if is_prime(i):
        lista_de_primos.append(i)
        print(i, "es primo")

print("Lista de primos:", lista_de_primos)

