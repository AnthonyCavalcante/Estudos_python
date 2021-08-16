num=int(input())

def fibonacci(n):
    li=[0,1]
    while len(li)<num:
        li.append(li[-1]+li[-2])
    for n in li:
        print(n)

fibonacci(num)