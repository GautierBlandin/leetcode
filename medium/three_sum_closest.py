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
        for i in range(min(occurrences[k], 3)):
            return_nums.append(k)
    return return_nums


def three_sum_closest(nums: list[int], target: int):
    # cleanup and sort nums array
    nums = cleanup(nums)
    nums = sorted(nums)

    n = len(nums)

    closest = float('inf')

    for i in range(n):
        p1 = i + 1
        p2 = n - 1
        while p1 < p2:
            three_sum = nums[i] + nums[p1] + nums[p2]
            if three_sum == target:
                return target
            if abs(target - closest) > abs(target - three_sum):
                closest = three_sum
            if three_sum < target:
                p1 += 1
            if three_sum > target:
                p2 -= 1
    return closest
