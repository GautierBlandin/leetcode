def compute_max_volume(l1_height, l2_height, l1_index, l2_index):
    """
    Compute the max volume of water between two lines.
    Args:
        l1_height: The height of the first line
        l2_height: The height of the second line
        l1_index: The index of the first line
        l2_index: The index of the second line

    Returns:
        The max volume of water between these lines
    """
    useful_height = min(l1_height, l2_height)
    width = abs(l1_index - l2_index)
    return useful_height * width


def max_amount_of_water(heights):
    i = 0
    j = len(heights) - 1
    max_volume = compute_max_volume(heights[i], heights[j], i, j)
    while i < j:
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
        max_volume = max(max_volume, compute_max_volume(heights[i], heights[j], i, j))
    return max_volume
