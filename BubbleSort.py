print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE YR. & SECTION: BSCOE 2-2\n")


def sort(nums):

    print(*nums)
    for i in range(len(nums)-1, 0, -1):
        for x in range(i):
            if nums[x] > nums[x+1]:
                temp = nums[x]
                nums[x] = nums[x+1]
                nums[x+1] = temp
            print(*nums)
    print()


nums = [82, 19, 8, 76, 86, 94, 60, 32, 21, 30]
sort(nums)
print(nums)