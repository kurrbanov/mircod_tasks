def solve():
    '''
    Идея: просто пройтись по списку и считать количество нулей, которое мы удалили.
    Длина списка будет уменьшаться на количество нулей, которое мы удалили, это нужно учитывать.
    '''
    
    a = list(map(int, input().split()))

    count_delete_zero = 0
    elem = 0
    size_a = len(a)

    while elem < size_a:
        if elem >= size_a - count_delete_zero:
            break
        if a[elem] == 0:
            del a[elem]
            count_delete_zero += 1
            continue
        elem += 1

    print(*a, sep=' ')


solve()