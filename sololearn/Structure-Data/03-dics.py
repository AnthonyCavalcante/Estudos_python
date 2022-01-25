def exercise1():
    contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
        }
    name = input()
    
    if name in contacts:
        result = contacts.get(name)
        print(result[1])
    else:
        print('not found')

def exercise2():
    points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
    ]
    result = [(x**2 + y**2)**0.5 for x,y in points]
    result.sort()
    print(result[0]) 


def exercise3():

    s1 = input()
    s2 = input()
    result = set(s1.split()) & set(s2.split())
    print(len(result))
    
#test
def ticket():
    #preco de 18 para cima = $20
    #preco menor de 18 é = $5
    data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18,
     "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11,
      "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, 
      "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59,
       "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27,
        "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, 
        "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, 
        "87-456": 8, "87-430": 40
        }
#age = int(input())
    adult = 0
    child = 0
    for i in data.values():
        if i <18:
            adult += 5
        else:
            child += 20
      
    

   
    



def main():
    ticket()

if __name__ == '__main__':
    main()
    