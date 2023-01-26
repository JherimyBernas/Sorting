print("\nPROGRAMMED BY: JHERIMY S. BERNAS")
print("COURSE YR. & SECTION: BSCOE 2-2\n")


def sort(nums):

    print(*nums)
    for i in range(1, len(nums)):
        temp = nums[i]
        x = i - 1

        while x >= 0 and temp < nums[x]:
            nums[x + 1] = nums[x]
            x -= 1
        nums[x + 1] = temp
        print(*nums)
    print()


nums = [82, 19, 8, 76, 86, 94, 60, 32, 21, 30]
sort(nums)
print(nums)
