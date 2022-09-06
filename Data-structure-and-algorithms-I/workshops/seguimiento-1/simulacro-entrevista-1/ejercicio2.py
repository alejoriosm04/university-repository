#Salta el repetido
def sumaGrupos(start, nums : str, i : int) -> int:
    if start == len(nums):
        return i
    elif start != len(nums)-1 and nums[start] == nums[start+1]:
        return sumaGrupos(start+2, nums, i)
    else:
        return sumaGrupos(start+1, nums, i+int(nums[start]))

nums = input()
print(sumaGrupos(0,nums,0))