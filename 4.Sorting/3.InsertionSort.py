def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = anchor

if __name__ == '__main__':
    elements = [3,45,2,34,1,5,4]
    insertion_sort(elements)
    print(elements)