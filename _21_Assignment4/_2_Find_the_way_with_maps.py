size=int(input("Please enter the size of a list: "))
lst=[]
for i in range(size):
    item=int(input("Enter element: "))
    lst.append(item)
print(end="\n")    
print("Original list: ", end="\n")
print(lst)
print(end="\n")

def triple(data):
     return data*3

triple_lst=list(map(triple,lst))
print("Triple of list numbers: ", end="\n")
print(triple_lst)
print(end="\n")
