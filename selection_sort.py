def selectionSort(list):
    for i in range(0, len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min=j
        list[i], list[min] = list[min], list[i]
    print(list)

selectionSort([1,3,4,2,5,8,7,6,9])

