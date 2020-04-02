#Program to remove duplicates of the list

my_list = [1,2,1,3,5,5,4]

unique_list = []

for i in my_list:
  if i not in unique_list:
    unique_list.append(i)
print(unique_list)