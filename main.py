# assuming my_list a Python list of tuples, 
# each tuple having 2 elements
for tuple_ in my_list:
    print(tuple_[0], tuple_[1])
    
# alternatively
for elem_1, elem_2 in my_list:
  print(elem_1, elem_2)
  
# for wider list use the * operator:
# my_list is assumed to be a list of tuple, each tuple with N elements
for a, *b in my_list:
  # now a is the first element of each tuple
  # while b is a list containing all other N-1 elements of the tuple
  print(a, b) 
  
# combinations are also allowed:
for a, *b, c in my_list:
  # a is the first element
  # b is a list of elements from the second to the previous-to-last one
  # c is the last element
  print(a, b, c)
  
# and so on...