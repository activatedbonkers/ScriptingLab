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
list1.append(42069)

print("The appended list is: \n", (list1))

#4.Delete an element from the list
list1.pop(-1)

print("The list after deleting an element is: \n", (list1))

#5.Determine if an element is present in the list.
exist_count = list1.count(4)
 
if exist_count > 0:
    print("Yes, 4 exists in list")
else:
    print("No, 4 does not exists in list")
