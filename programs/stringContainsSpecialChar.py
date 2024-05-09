import re

str = "welcome @!$%python"

regex = re.compile('[~!@#$%^&><,"{}./;\=-]')

if (regex.search(str) == None):
    print("No special characters are present")
else:
    print("special characters present")
