var=input()
count= var.split(" ")
Text=[]
indexText=[]
for n in count:
    x=(len(n))
    Text.append(n)
    indexText.append(x)
print(Text[indexText.index(max(indexText))])
