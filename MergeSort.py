print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE YR. & SECTION: BSCOE 2-2\n")


def sort(nums):

    print(*nums)
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        sort(left)
        sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k]=right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    print(*nums)


print()
nums = [82, 19, 8, 76, 86, 94, 60, 32, 21, 30]
sort(nums)
print(nums)
