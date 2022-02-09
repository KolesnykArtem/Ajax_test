def Sec_larg(nums):
    nums.sort()
    return(nums[-2])

list_num = []

for i in range(int(input())):
    list_num.append(input())
print(Sec_larg(list_num))