def selection_sort(data):
    for i in range(0,len(data)):
        min = i
        for j in range(i,len(data)):
            if data[j]<data[min]:
                min=j
        if min!=i:
            temp=data[i]
            data[i]=data[min]
            data[min]=temp
    return data

print selection_sort([2,5,4,3,2,6,7])
