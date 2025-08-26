#making the empty list
my_list = []

#appending values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#adding a number at a specified index
my_list.insert(1, 15)
 #adding another list by extension
my_list2 = [50, 60, 70]
my_list.extend(my_list2)


#removing elements from a list
my_list.remove(70)

#sorting the list
my_list.sort()

#finding and printing the index of value 30
index = my_list.index(30)
print(index)