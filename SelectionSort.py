

def sort(nums):

    for i in range(5):
        min_pos = i
        for x in range(i, 6):
            if nums[x] < nums[min_pos]:
                min_pos = x

        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp
        print(nums)


nums = [82, 19, 8, 76, 86, 94, 60, 32, 21, 30]