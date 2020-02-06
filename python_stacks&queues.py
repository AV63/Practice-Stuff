#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Pallindrome using stack and queue

# In[4]:


from collections import deque
import sys


# In[9]:


class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = deque()
    def push(self,character):
        self.stack.append(character)
    def pop(self):
        return self.stack.pop()
    def enqueue(self,character):
        self.queue.append(character)
    def dequeue(self):
        return self.queue.popleft()
        
s = input('Enter a string : ')
obj = Solution()

isPallindrome = True

for i in s:
    obj.push(i)
    obj.enqueue(i)
    
for i in range(len(s)//2):
    if obj.pop() != obj.dequeue():
        isPallindrome = False
    
if isPallindrome:
    print('Pallindrome!')
else:
    print('Not a pallindrome!')


# In[ ]:





# In[ ]:




