def inverter_string(texto):
    return texto[::-1]

#usuário entra com um texto
entrada = input("Digite um string: ")
print(f"O texto invertido é: {inverter_string(entrada)}")