"""
Exercício 2: Soma de Números em uma Lista Aninhada
Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a
soma de todos os números em uma lista, mesmo que os números estejam dentro de
sublistas (listas aninhadas).
Exemplo de Entrada:
soma_lista_aninhada([1, [2, 3], [4, [5]]])
Saída Esperada:
15 # (1 + 2 + 3 + 4 + 5)
Dica: Verifique se o elemento atual é uma lista ou um número para decidir se deve
continuar a recursão.

"""
def soma_lista_aninhada(lista):
    # Caso base: se a lista estiver vazia, a soma é 0
    if not lista:
        return 0

    # Pega o primeiro elemento da lista
    primeiro = lista[0]

    # Verifica se o elemento atual é uma lista
    if isinstance(primeiro, list):
        # Se for uma lista, chama a função recursivamente para somar os elementos internos
        return soma_lista_aninhada(primeiro) + soma_lista_aninhada(lista[1:])
    else:
        # Se for um número, soma o número e continua a recursão com o restante da lista
        return primeiro + soma_lista_aninhada(lista[1:])

# Testando a função com o exemplo fornecido
entrada = [1, [2, 3], [4, [5]]]
resultado = soma_lista_aninhada(entrada)

# Exibindo o resultado
print(f"A soma dos números na lista aninhada {entrada} é: {resultado}")
