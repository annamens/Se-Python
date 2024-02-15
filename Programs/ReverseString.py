s = 'radar'
temp=s
rev = ""
for i in range(len(s)-1,-1,-1):
    rev = rev +s[i]

print(rev)

if rev == s:
    print("string is palindrome")
else:
    print("string is not palindrome")
