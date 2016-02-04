def insertion_sort(data):
    if len(data)<=1:
        return data
    for i in range(1,len(data)):
        key = data[i]
        j=i-1
        while(j>=0 and data[j]>key):
            data[j+1]=data[j]
            j=j-1
        data[j+1]=key
    return data

print insertion_sort([3,4,2,6,7,1,2])
