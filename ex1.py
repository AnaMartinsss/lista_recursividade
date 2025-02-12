"""
    Exercício 1: Reverter os Caracteres de uma String
Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
string s e devolve a string invertida. Não use laços (for ou while).

"""
def reverter_caracteres(s):
    # Caso base: o local de parada da recursão
    # Se a string tem 0 ou 1 caracteres, não precisa mais dividir, ela já está invertida
    if len(s) <= 1:
        return s
    else:
        # Último caractere da string (s[-1]) é concatenado com o resultado
        # da chamada recursiva para o restante da string (s[:-1])
        return s[-1] + reverter_caracteres(s[:-1])

# Testando a função
string_original = "Exemplo"  # String inicial
string_invertida = reverter_caracteres(string_original)  # Chamando a função para inverter a string

# Exibindo os resultados
print("String original:", string_original)  # Exibe a string antes de inverter
print("String invertida:", string_invertida)  # Exibe a string depois de inverter

