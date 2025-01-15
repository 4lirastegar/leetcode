# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

def isPalindrome(s):
  s=s.lower()
  firstPointer=0
  lastPointer= len(s)-1
  while firstPointer < lastPointer:
    while not s[firstPointer].isalnum() and firstPointer<lastPointer:
      firstPointer+=1
    while not s[lastPointer].isalnum() and firstPointer<lastPointer:
      lastPointer-=1
    if s[firstPointer]==s[lastPointer]:
      firstPointer+=1
      lastPointer-=1
    else:
      return False

  return True




s="A man, a plan, a canal: Panama"
print(isPalindrome(s))