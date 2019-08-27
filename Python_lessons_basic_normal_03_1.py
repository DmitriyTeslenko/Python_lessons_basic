def fibonacci(n, m):
    listfib=[1, 1]
    for i in range(m):
        listfib.append(listfib[-2]+listfib[-1])
    return listfib [(n-1):m]    

print(fibonacci(2, 20))
