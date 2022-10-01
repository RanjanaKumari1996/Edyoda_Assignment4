size=int(input("Please enter the size of a list: "))
lst=[]
for i in range(size):
    item=int(input("Enter element: "))
    lst.append(item)
print(end="\n")    
print("Original list: ", end="\n")
print(lst)
print(end="\n")

def square(data):
    return data**2

sq_lst=list(map(square,lst))
print("Square the elements of the list: ", end="\n")
print(sq_lst)
print(end="\n")