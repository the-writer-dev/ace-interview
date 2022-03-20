# in graph
# if a cycle exists, we can detect the cycle in 2 steps
# 1. slow and fast pointer, which slow advances one node each unit of time while fast advances two nodes each unit of time
#    so, the fast will catch up the slow 
# 2. put either slow and fast pointer to the first position of the graph
#    advance both one node each unit of time and the meeting point is the starting point of the cycle

# proof
# let's say slow travels only x + y and fast travels x + y + z + y where they meet at y 
# fast is fast as twice as slow, so the equation would be 2 (x + y) = x + 2y + z => x = z hence moving one pointer 
# to the first point of graph works

# related topic (you can find either in this repo or Leetcode)
# linked list cycle 
# linked list cycle 2 
# duplicated numbers
