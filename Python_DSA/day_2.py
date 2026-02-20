def largest_substring(str1):
    left=0
    start=0
    window=set()
    max_length=0

    for right in range(len(str1)):
        current_char = str1[right]
        while current_char in window:
            window.remove(str1[left])
            left+=1
        window.add(current_char)

        if right-left+1 > max_length:
            max_length = right-left+1
            start = left

    return str1[start:start+max_length]

print(largest_substring("abcabcdefbb"))


def anagram_check(s,t):

    if len(s) != len(t):
        return False

    count = {}
    for ele in s:
        count[ele] = count.get(ele,0)+1

    for char in t:
        if char not in count:
            return False

        count[char]-=1

        if count[char]==0:
            del count[char]

    return True

print(anagram_check("listen","silent"))




