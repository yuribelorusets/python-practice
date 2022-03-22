def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count = {num: nums.count(num) for num in nums}

    most_common = 0
    for elem in count:
        if count[elem] > most_common:
            most_common = elem
    return most_common