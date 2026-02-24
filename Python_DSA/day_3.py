def largest_container(arr):

    left = 0
    right = len(arr)-1
    max_area = 0
    base_left = base_right =0

    while left<right:
         height = min(arr[left],arr[right])
         width = right-left
         area = height * width

         if area > max_area:
             max_area = area
             base_left = left
             base_right = right

         if arr[left] < arr[right]:
             left += 1
         else:
             right -= 1

    return arr[base_left], arr[base_right], max_area

arr = [1,2,3,4,6,6,4,8,2,9]
print(largest_container(arr))


def reverse_num(num):
    reverse =0
    digit=0
    while num > 0:
        digit = num%10
        reverse = reverse*10+digit
        num = num//10

    return reverse

print(reverse_num(12345))


