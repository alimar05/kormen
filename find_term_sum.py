from binary_search import binary_search


def find_term_sum(array, x):
    
    lst_terms = []
    for i, a in enumerate(array):
        j = binary_search(array, x-a, 0, len(array)-1)
        if j:
            lst_terms.append((i, j))
    
    return lst_terms
        

if __name__ == '__main__':
    array = [4, 5, 6, 2, 3, 8]
    print(find_term_sum(array, 11))
