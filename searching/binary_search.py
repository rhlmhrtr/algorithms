# Hello World program in Python

"""def binary_search(list,n):
    low=0
    upper=len(list)
    while(low<=upper):
        mid=(low+upper)/2
        if list[mid]==n:
            return "Element %d found at position %d" %(n,mid+1)
        if list[mid]<n:
            low=mid+1
        if list[mid]>n:
            upper=mid-1
    return "Element %d not found" %(n)


print binary_search([1,2,3,4,5,6,7],0)"""

def binary_search(list,lb,ub,n):
    if (lb<=ub):
        mid=(lb+ub)/2
        if list[mid]==n:
            return "Element %d found at position %d" %(n,mid+1)
        if list[mid]<n:
            return binary_search(list,mid+1,ub,n)
        if list[mid]>n:
            return binary_search(list,lb,mid-1,n)
    else :
        return "Element %d not found" %(n)

print binary_search([1,2,3,4,5,6,7],0,7,3)
