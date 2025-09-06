"""Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list."""

# Empty list
my_list=[]
# Appending my list
my_list.extend([10,20,30,40])
# Inserting 15 at second index
my_list.insert(2,15)
# Extending my_list with another list
my_list.extend([50,60,70])
# Removing last element from the list.
my_list.pop(-1)
# sorting in a ascending order
my_list.sort()
# Finding index of value 30
list=my_list.index(30)
print(list)  #Index 3
print(my_list) #Printing my list
print (len(my_list)) #Printing my length list