ransomNote="a"
magazine="b"
a=set(ransomNote)
for i in a:
    x=ransomNote.count(i)
    y=magazine.count(i)
    if y<x:
        print(False)
        break
    else:
        print(True)