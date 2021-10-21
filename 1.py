#1.Create list with inputs from user
list1 = []
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    element = int(input())
 
    list1.append(element)
     
print("The list is:\n", (list1))

#2.Determine minimum and maximum elements in the list
print("The Smallest Element in this List is : ", min(list1))
print("The Largest Element in this List is : ", max(list1))

#3.Insert new element into the list
o = int(input("Enter the element to be appended : "))
list1.append(o)

print("The appended list is: \n", (list1))

#4.Delete an element from the list
p = int(input("Enter the index number of the element to be popped: "))
list1.pop(p)

print("The list after deleting an element is: \n", (list1))

#5.Determine if an element is present in the list.
q = int(input("enter an element to check if it is present in the list "))

 
if (q in list1):
    print ("Element Exists")
