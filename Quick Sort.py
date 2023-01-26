print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE YR. & SECTION: BSCOE 2-2\n")


def partition(nums, first, last):
    pivot = nums[last]
    i = first - 1
    for j in range(first, last):
        if nums[j] <= pivot:
            i = i + 1
            (nums[i], nums[j]) = (nums[j], nums[i])
    (nums[i + 1], nums[last]) = (nums[last], nums[i + 1])
    print(*nums)
    return i + 1


def sort(nums, first, last):
    if first < last:
        sub_array = partition(nums, first, last)
        sort(nums, first, sub_array - 1)
        sort(nums, sub_array + 1, last)


nums = [82, 19, 8, 76, 86, 94, 60, 32, 21, 30]
print(*nums)
sort(nums, 0, len(nums) - 1)
print()
print(nums)

