
import re
lst = 'Smoke Testing is@ the basic testing, in the Testing proccess.'
txt = re.sub(r"[,=-@%.]","",lst)
print(txt)
txt = txt.strip("").lower().split()
count = {}

for word in txt:
    if word in count:
        count[word]  = count[word]+1
    else:
        count[word] =1


print(count)