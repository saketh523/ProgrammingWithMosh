my_list = [10,20,1000,5000,1]
max = my_list[0]
len1 = len(my_list)
for i in range(len1):
  if(my_list[i] > max):
    max = my_list[i]
print(max)
