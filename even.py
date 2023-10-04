n = int(input("enter a number:"))
if n % 2==0:
    print("n is even")



#palindrom
def isPalindrome(str):
    for i in range( 0 , int(len(str))):
        if str[i] != str[len(str)-len(str)]:
            return False
    return True
n = "saibhavani"
ans = isPalindrome(n)

if (ans) :
    print("Yes")
else:
    print( " No ")