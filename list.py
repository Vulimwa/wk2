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
