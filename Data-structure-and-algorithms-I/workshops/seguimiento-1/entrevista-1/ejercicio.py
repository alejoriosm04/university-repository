#Divide el arreglo
def sumaGrupos(nums : list, meta1 : int, meta2 : int, i : int):
    if len(nums) == i:
        return meta1 == meta2
    else:
        return sumaGrupos(nums, meta1+nums[i], meta2, i+1) or sumaGrupos(nums, meta1, meta2+nums[i], i+1)

n = int(input())
nums = [0]*n
for i in range(n):
	nums[i] = int(input())
print(sumaGrupos(nums,0,0,0))