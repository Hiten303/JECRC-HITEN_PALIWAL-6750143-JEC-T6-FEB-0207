# input: [10,2.2,5,'Hello',[100,200],99.9]
# output: 99.9

# input {'a':1,'b':2,'c':3,'d':4}
# output {1:'a',2:'b',3:'c',4:'d'}


# input('Hello','Hi',20,40.2,9.6j,[1,2],'python',(1,2,3))
# output {'Hello':'1','Hi':'Hi','PYTHON':'py',(1,2,3):2}


# coll = [1,'HELLO',3.2,[1,2,3]]
# max = coll[0]
# for i in coll:
#     if type(i) in [int,float]:
#         if i > max:
#             max = i
# print(max)

# coll = {'a':1,'b':2}
# new_coll = {}
# for i in coll:
#     new_coll[coll[i]]=i

# print(new_coll)

coll = ('Hello','Hi',20,40.2,9.6j,[1,2],'PYTHON','JECRC',(1,2,3))
new_coll = {}

for i in coll:
    if type(i) in [str, tuple]:
        if len(i) % 2 == 0:
            new_coll[i]=i[0]+i[-1]
        else:
            new_coll[i]=i[len(i)//2]
print(new_coll)
