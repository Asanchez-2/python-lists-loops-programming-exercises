arr = [45, 67, 87, 23, 5,  32, 60]
#your code below:
# arr.reverse()
# print(arr)
arr_lenght = len(arr)-1
new_list_variable = []
for i in range(6,-1,-1):
    new_list_variable.append(arr[i])
print(new_list_variable)
