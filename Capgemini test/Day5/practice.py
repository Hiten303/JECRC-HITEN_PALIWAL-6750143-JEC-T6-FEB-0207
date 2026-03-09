def Twosum(list1,target):
    length=len(list1)
    for i in range(0,length):
        for j in range(i+1,length):
            if list1[i]+list1[j]==target:
                return ((i,j))

val=Twosum([1,2,5],4)
print(val)