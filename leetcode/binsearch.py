# def findMin(nums: list[int]) -> int:


#     l = 0
#     r = len(nums) - 1

#     while l < r:

#         mid = (l + r) // 2

#         if nums[mid] > nums[r]:
#             l = mid + 1
#         else:
#             r = mid

    
#     return min(nums[r], nums[l])

# print(findMin([3,4,5,6,1,2]))


def search(nums: list[int], target: int):

    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    if nums[l] <= target <= nums[-1]:
        l, r = l, len(nums) - 1
    else:
        l, r = 0, l - 1

    while l < r:

        mid = (l + r) // 2

        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    if nums[l] == target:
        return l
    else:
        return -1
    






def absolutePermutation(n, k):
    
    used = set()
    
    perm = []
    
    for i in range(1, n + 1):
        
        if i - k < 1:
            p = i + k
        else:
            p = i - k
        
        if p > n:
            return [-1]
        
        perm.append(p)
                
    print(perm)
    return perm

absolutePermutation(10, 1)

