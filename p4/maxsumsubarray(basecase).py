lm=[5,4,-1,7,8]
ll=[-1,1,-3,4,1,4,1,-5,4]
l = [-5, -4, 10, 20, -1]
l = [100, -50, 10, 20, -1]
nums = [-2,1,-3,4,-1,2,1,-5,4]
num1=[-2,1,-3,4,-1,2,1,-5,4]
num2=[2,0,3,-2]
num3=[5,4,-1,7,8]
def max_sum_subarray(array):
  mid=len(array)//2
  left=split(array[0:mid+1],0)
  right=split(array[mid+1:len(array)],mid+1)
  cross_array=max_cross_subarray(array,0,len(array)//2,len(array)-1)


  max_val=max(right[0],left[0],cross_array[0])
  if max_val in left:
    low=left[1]
    high=left[2]
  elif max_val in right:
    low=right[1]
    high=right[2]
  else:
    low=cross_array[1]
    high=cross_array[2]
  print(max_val,left,right,cross_array)
  print('Max value is',max_val,' and the subarray is',array[low:high+1])
def split(array, offset=0):
    n = len(array)
    if n == 0:
        return float('-inf'), -1, -1
    if n == 1:
        return array[0], offset, offset
    if n == 2:
        sums = [(array[0], 0, 0), (array[1], 1, 1), (array[0]+array[1], 0, 1)]
        max_sum, low, high = max(sums, key=lambda x: x[0])
        return max_sum, low + offset, high + offset


    mid = n // 2
    left_val, left_low, left_high = split(array[:mid], offset)
    right_val, right_low, right_high = split(array[mid:], offset + mid)
    cross_val, cross_low, cross_high = max_cross_subarray(array, 0, mid-1, n-1)
    cross_low += offset
    cross_high += offset


    if left_val >= right_val and left_val >= cross_val:
        return left_val, left_low, left_high
    elif right_val >= left_val and right_val >= cross_val:
        return right_val, right_low, right_high
    else:
        return cross_val, cross_low, cross_high
def max_cross_subarray(array, low, mid, high):
    left_sum = float('-inf')
    ssum = 0
    max_left = mid
    for i in range(mid, low-1, -1):
        ssum += array[i]
        if ssum > left_sum:
            left_sum = ssum
            max_left = i


    right_sum = float('-inf')
    ssum = 0
    max_right = mid + 1
    for j in range(mid+1, high+1):
        ssum += array[j]
        if ssum > right_sum:
            right_sum = ssum
            max_right = j


    return left_sum + right_sum, max_left, max_right
max_sum_subarray(l)
max_sum_subarray(lm)
max_sum_subarray(num2)
