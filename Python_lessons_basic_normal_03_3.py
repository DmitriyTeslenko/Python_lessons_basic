
mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
def my_filter(func, sequence):
    list_2 = [a for a in sequence if func]
    return list_2
print (list(filter(lambda x: x == 'мак', mixed)))
