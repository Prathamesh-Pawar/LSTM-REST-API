#Input Number
n = input()
count = 1
old_count = 0
new_count = 1
new_list = []

#Create a arithmetic series of numbers
Input = list(range(1, int(n) + 1))

#Divide them into sub lists with a an arithmetic progression
for i in Input:
    new_list.append(Input[old_count:new_count])
    count += 1
    old_count = new_count
    new_count = count + new_count
new_list = [i for i in new_list if len(i) > 0]
final_list = []

#Format the list in desired structure
for i in range(len(new_list) - 1, 0, -1):
    if len(new_list[i]) > len(new_list[i - 1]):
        final_list.append(new_list[i])
final_list.append([1])

#Print it
final_list = '\n'.join([' '.join([str(j) for j in i]) for i in final_list])
print(final_list)
