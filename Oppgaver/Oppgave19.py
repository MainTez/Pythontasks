def delete_duplicates(lst):
    return list(set(lst))  # Turn list into set to remove duplicates, then turn it back into a list

My_List = [1, 2, 3, 4, 4, 5, 2, 6, 1]  # Your original list with duplicates
Unique_list = delete_duplicates(My_List)  # Remove duplicates using the function

print("List without duplicates --> ", Unique_list)  # Print the new list
