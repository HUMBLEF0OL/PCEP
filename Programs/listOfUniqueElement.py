my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

output = []

for i in my_list:
    if i not in output:
        output.append(i)

print(output)