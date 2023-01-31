# link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# idea: concatenate two linked list -> (a+b) and (b+a)
# if a and b has intersection, we return that node
# else we return null
def find_intersection(a, b):
    if a == None or b == None:
        return None

    while a != b:
        a = a.next if a else b
        b = b.next if b else a
    return a
