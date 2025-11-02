def max_subarray_under_constraint(resources, constraint):
    n = len(resources)
    if n == 0 or constraint <= 0:
        return None  

    best_sum = float('-inf')
    best_range = None  

    left = 0
    current_sum = 0

    for right in range(n):
        current_sum += resources[right]

        
        while current_sum > constraint and left <= right:
            current_sum -= resources[left]
            left += 1

        
        if current_sum <= constraint and current_sum > best_sum:
            best_sum = current_sum
            best_range = (left, right)

    if best_range is None:
        return None
    else:
        start, end = best_range
        return resources[start:end + 1], best_sum
