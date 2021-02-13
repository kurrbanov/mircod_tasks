lst_1 = list(map(int, input().split())) # Ввод первого списка
lst_2 = list(map(int, input().split())) # Ввод второго списка


def solve_first_way():
    global lst_1, lst_2
    result_array = []
    '''
    Первая идея решения: отсортировать второй список, циклом пройтись по элементам первого списка и
    с помощью бинарного поиска найти текущий элемент во втором списке.
    Пусть N - длина первого списка, M - длина второго списка.
    Тогда асимптотика будет: O(logM + N*logM) ~ O(N*logM)
    '''

    lst_2.sort()

    def binary_search(elem, lst):
        left, right = 0, len(lst) - 1

        while right - left > 1:
            mid = (right + left) // 2
            if lst[mid] < elem:
                left = mid + 1
            elif lst[mid] > elem:
                right = mid - 1
            else:
                return True
        
        if lst[left] == elem or lst[right] == elem:
            return True
        else:
            return False

    for element in lst_1:
        if not binary_search(element, lst_2):
            result_array.append(element)
    
    return result_array


print("Результат первого способа решения: ")
print(*solve_first_way(), sep=' ') # вывод результата первого способа решения 


def solve_second_way():
    '''
    Второй способ решения работает только при условии, что элементы внутри списка не будут повторяться.
    Просто нужно будет из двух списков сделать два множества и найти отличия первого множества от второго.
    Пусть N - длина первого списка.
    Тогда асимптотика будет: O(N)
    '''

    set_lst_1 = set(lst_1)
    set_lst_2 = set(lst_2)

    return list(set_lst_1 - set_lst_2)


print("Результат второго метода решения:")
print(*solve_second_way(), sep=' ') 
