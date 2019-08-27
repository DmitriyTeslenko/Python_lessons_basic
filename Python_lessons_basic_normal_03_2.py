
def list_sort(lst):
    if isinstance(lst, list):
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if lst[i]<lst[j]:
                    lst[j:j]=[lst.pop(i)]  
        return(lst)
    else:
        print('list_sort argument is not "list" type ')

print(list_sort([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
