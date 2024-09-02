def bubble_sort(arr):
    n = len(arr)
    # Passa por todos os elementos da lista
    for i in range(n):
        # A última parte da lista já está ordenada
        for j in range(0, n-i-1):
            # Troca se o elemento encontrado for maior do que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Lista de exemplo
lista = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", lista)
lista_ordenada = bubble_sort(lista)
print("Lista ordenada:", lista_ordenada)