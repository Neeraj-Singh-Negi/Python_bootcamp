#LIST

friendname=["pawan","Ivan","Anshu"]
print("Before",friendname)
# Add a name in list
friendname.append("Neeraj")
print("After",friendname)
friendname.insert(0,"Harsh")
print("Add name at index 0",friendname)

# Remove name from list

friendname.remove("Harsh")
print(friendname)

# CLEAR THE LIST

friendname.clear()
print(friendname)

# To remove data in list from specific index

friendname.pop(2)
print(friendname)

# To sort the data

friendname.sort()
print(friendname)

# To print element in the given list

for names in friendname:
    print(names)
