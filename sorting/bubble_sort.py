def bubble_sort(data):
    for i in range(1,len(data)):
        print data
        for j in range(0,len(data)-i):
            if data[j]>data[j+1]:
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    return data
