my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
my_sample_list[1]= 'Steven'
my_sample_list_lenght = len(my_sample_list)-1
my_sample_list[my_sample_list_lenght] = 'Pepe'
my_sample_list[0] = my_sample_list[2]+my_sample_list[4]
# print(my_sample_list[1])
for i in range(my_sample_list_lenght,-1,-1):
    print(my_sample_list[i])