def sumaGrupos(start, nums : list, k :int) -> bool:
    if k == 0:
        return True
    elif start == len(nums):
        return False
    
    if start != len(nums)-1:
        return sumaGrupos(start+2, nums, k-nums[start]) or sumaGrupos(start+1, nums, k)
    else:
        return sumaGrupos(start+1, nums, k) or sumaGrupos(start+1, nums, k-nums[start])



n = int(input())
nums = [0]*n
for i in range(n):
	nums[i] = int(input())
k = int(input())
print(sumaGrupos(0,nums,k))