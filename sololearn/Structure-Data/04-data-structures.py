#exercise 1
class Browser:
    def __init__(self):
        self.links = []  
  
    def is_empty(self):
        return self.links == []
  
    def push(self, link):
        self.links.insert(0, link)
    
    def pop(self):
        print(self.links.pop())
      
    
    def print_links(self):
        print(self.links)
'''x = Browser()
    x.push('about:blank')
    x.push('www.sololearn.com')
    x.push('www.sololearn.com/courses/')
    x.push('www.sololearn.com/courses/python/')
    while not x.is_empty():
        x.pop()'''
#end of exercise 1 =============

#exercise 2

class CallCenter:
    def __init__(self):
        self.customer= []

    def is_empty(self):
        return self.customer ==[]
        

    def enqueue(self, user):
        self.customer.insert(0, user)

    def dequeue(self):
        return  self.customer.pop()
          
'''time = {'general': 5, 'technical': 10}
    time_final = 0
    call = CallCenter()

    while True:
        user = input()  
        time_final += time.get(user, 0)
        if user == 'end':
            break
        call.enqueue(user)
        user = ''
        
    print(call.customer)

    while not call.is_empty():
        print(call.dequeue())
      
    print(call.customer)
    print(time_final)'''
#end of exercise2==========

#exercise3
class Track:
    def __init__(self, title, next):
        self.title = title
        self.next = next


class Player:
    def __init__(self):
        self.head = None
    
    def add(self, title):
        if not self.head:
            self.head = Track(title, None)
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Track(title, None)

    def print_track(self, title):
       self.title = title
       return self.title
    
'''p = Player()
    while True:
        x = input()
        if x == 'end':
            break
        p.add(x)   
        print(p.print_track(x))        
'''
# end of exercise 3=====================        
#Final test
class AnalyseStack:
    def __init__(self) :
        self.exp = []
    
    def add(self, item):
        self.exp.append(item)
        return
    def remove(self):
        return self.exp.pop(0)
    
    

def main():
    x = AnalyseStack()
    balanced = ''
    while True:
        expression = input()
        if expression[0] !=")":
            break
        print('expressão incorreta')
    for item in expression.replace(" ",""):
        x.add(item)
    
    if x.exp.count('(') == x.exp.count(')'):
        balanced = True
    else:
        balanced = False
    
    while len(x.exp) > 0:
        x.remove()
    
    print(balanced)

if __name__ == '__main__':
    main()
    