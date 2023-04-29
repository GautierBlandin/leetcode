def three_sum(nums):
    nums = cleanup(nums)
    n = len(nums)

    if n < 3:
        return []

    nums.sort()
    triplets = []
    for i in range(n):
        if i > 0:
            if nums[i-1] == nums[i]:
                continue
        p1 = i + 1
        p2 = len(nums) - 1
        while p1 < p2:
            two_sum = nums[p1] + nums[p2]
            if two_sum < -nums[i]:
                p1 += 1
            elif two_sum > -nums[i]:
                p2 -= 1
            else:
                triplets.append([nums[i], nums[p1], nums[p2]])
                if nums[p1 + 1] == nums[p1]:
                    p1 += 2
                else:
                    p1 += 1
                if nums[p2 - 1] == nums[p2]:
                    p2 -= 2
                else:
                    p2 -= 1
    return triplets


def cleanup(nums: list[int]):
    n = len(nums)
    occurrences = {}
    for i in range(n):
        if nums[i] in occurrences:
            occurrences[nums[i]] += 1
        else:
            occurrences[nums[i]] = 1

    return_nums = []
    for k in occurrences:
        if k == 0:
            for i in range(min(occurrences[k], 3)):
                return_nums.append(k)
        else:
            for i in range(min(occurrences[k], 2)):
                return_nums.append(k)
    return return_nums
