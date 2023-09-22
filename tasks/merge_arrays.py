def merge(nums1, m, nums2, n):
    # counters for nums1 and nums2
    i = m - 1
    j = n - 1
    k = m + n - 1

    # looping untill there are elements in both arrays nums1 and nums2
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # if there are elements in nums2 we need to copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# data for test
nums1 = [1, 2, 6, 8, 0, 0, 0, 0]
m = 4
nums2 = [2, 5, 6, 7]
n = 4
merge(nums1, m, nums2, n)
print(nums1)