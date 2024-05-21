

with open('notes.txt','r') as file:
    lines=file.read()
    words= len(lines)
    print(words)