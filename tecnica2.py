def pertence_fibonacci(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b 
    return False

#usuário entra com um número
num = int(input("Digite um número: "))

#verifica se o número pertence a sequência
if pertence_fibonacci(num):
    print(f"{num} pertence a sequência de Fibonacci")
else:
    print(f"{num} não pertence a sequência de Fibonacci")