print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE YR. & SECTION: BSCOE 2-2\n")


def sort(nums):

    print(*nums)
    for i in range(0, len(nums)-1):
        min_pos = i
        for x in range(i, 10):
            if nums[x] < nums[min_pos]:
                min_pos = x

        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp
        print(*nums)
    print()


nums = [82, 19, 8, 76, 86, 94, 60, 32, 21, 30]
sort(nums)
print(nums)