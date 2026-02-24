def largest_num(arr):
    if len(arr) == 0:
        return None

    max_ele = arr[0]

    for num in arr:
        if num > max_ele:
            max_ele = num

    return max_ele

arr = [5,15,55,66,25,35,35]
arr1 = [-5, -10, -2]
print(largest_num(arr))
print(largest_num(arr1))


def second_largest(second_arr):
    if len(second_arr) < 2:
        return None
    max_num = second_max = float('-inf')

    for ele in second_arr:
        if ele > max_num:
            second_max = max_num
            max_num = ele
        elif ele > second_max and ele != max_num:
            second_max = ele

    if second_max == float('-inf'):
        return None

    return second_max
second_arr = [-10, -20, -30, -5]
print(second_largest(second_arr))

def remove_duplicates(dup_list):
     slow = 0
     for fast in range(1 , len(dup_list)):
         if dup_list[fast]!= dup_list[slow]:
             slow+= 1
             dup_list[slow] = dup_list[fast]

     return (slow+1)

dup_list = [1,1,2,2,2,3,3,4,5,5,5,6,7,7]
k = remove_duplicates(dup_list)
print(dup_list[:k])


def move_zeros_to_end(arr):
     slow = 0
     for fast in range(len(arr)):
         if arr[fast]!= 0:
             arr[slow],arr[fast] = arr[fast],arr[slow]
             slow+=1

     return arr

arr = [1,0,2,3,0,0,4,5,0,0]
move_zeros_to_end(arr)
print(arr)

def two_sum(nums,target):
    seen ={}
    new_list=[]
    new=[]

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            new_list.extend([[complement, nums[i]]])
            new.extend([(seen[complement],i)])

        seen[nums[i]] = i
    print(new_list)
    print(new)

arr = [2,7,6,3,5,9,4,5]
target = 10

print(two_sum(arr,target))



