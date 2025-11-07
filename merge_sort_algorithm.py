def merge_sort(array: list) -> list:
    """Ordena una lista utilizando el algoritmo 'Merge Sort'."""
    if len(array) <= 1:
        return array
    # Dividir el arreglo en 02 mitades
    middle = len(array) // 2
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])
    # Combinar las 02 mitades ordenadas
    return merge(left_half, right_half)

def merge(left: list, right: list) -> list:
    """Combina dos listas ordenadas en una sola lista ordenada."""
    merged = []
    i = j = 0
    # Comparar y mezclar elementos
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Añadir los elementos restantes
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:' + str(numbers))
    sorted_numbers = merge_sort(numbers)
    print('Sorted array: ' + str(sorted_numbers))
merge_sort(numbers)
