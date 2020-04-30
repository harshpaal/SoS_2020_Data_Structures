import sys

class Solution:
    # Write your code hered
    def __init__(self):
        self.stack = []
        self.queue = []
    
    def pushCharacter(self, elem):
        self.stack.append(elem)
    def enqueueCharacter(self, elem):
        self.queue.append(elem)

    def popCharacter(self):
        if len(self.stack)!=0:
            return self.stack[len(self.stack)-1]
        else:
            print("Error: List out of index")
    def dequeueCharacter(self):
        if len(self.queue)!=0:
            return self.queue[0]
        else:
            print("Error: List out of index")



# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
