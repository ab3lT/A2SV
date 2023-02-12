
def sorting(num):
    for i in range(len(num)-1):
        minPos = i
        for j in range(i, len(num)):
            if num[j] < num[minPos]:
                minPos = j
        temp = num[i]
        num[i] = num[minPos]
        num[minPos] = temp
        print(num)
num = [7,1,6,3,8,5]
sorting(num)
