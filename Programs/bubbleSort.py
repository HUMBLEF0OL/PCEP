arrList = [5,3,7,1,9]

# take input
# while True:
#     currentValue = int(input("Enter list member: "))
#     if currentValue == -1:
#         break
#     else:
#         arrList.append(currentValue)

# bubble sort algorithm

for i in range(len(arrList) -1):
    flag = False
    for j in range(len(arrList) -1):
        if arrList[j] < arrList[j+1]:
            temp = arrList[j]
            arrList[j] = arrList[j+1]
            arrList[j+1] = temp
            flag = True
    if flag == False:
        break

print(arrList)