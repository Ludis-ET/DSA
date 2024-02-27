myList = [1,2,3,4]

myList[3] = 100 #  updating the value of an existing element ->  O(1)

print("Accessed: ", myList[3]) # accessing the updated value -> O(1)

myList.insert(1,2) # adding an element at a specific position -> O(n)

myList.append(12) # adding an element to the end of the list -> O(1)

myList.extend([1,2,3]) # adding an  iterable (list, tuple etc.) elements to the end of the list -> O(k), where k is the size of the iterable

print(myList) # printing the entire list -> O(n)

print(myList[2:4]) #  slicing the list from index 2 to 4 (not inclusive) -> O(k), where  k is the length of the slice

myList.pop(1) # removing an element by its index -> O(n)

myList.pop() # removing the last element -> O(1)