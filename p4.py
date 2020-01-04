def chota(alist):
    for i in range(len(alist)-1):
        if alist[i]>alist[i+1]:
            a=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=a
    return(alist)

alist = [1325,344,464,5343,73636]
print(chota(alist))
