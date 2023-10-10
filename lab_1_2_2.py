def modif(x):
    return (bin(x)[2:].count("1"))

nums = list(input().split(" "))
nums = [int(x) for x in nums]
nums.sort()
nums.sort(key=modif)
print(nums)