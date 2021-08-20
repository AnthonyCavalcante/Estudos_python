class Animal:

    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
        self.real= 0
    
    def detail(self):
        return "o " + self.__class__.__name__+ " se chama " + self.name +"\nde cor " \
            + self.color +"\na idade real é "+ str(self.real) + " anos"
    
    def grito(self):
        return self.detail()
        

class Dog(Animal):
    def grito(self):
        self.real = int(self.age) * 7 
        return self.detail()

class Cat(Animal):
    def grito(self):
        x= int(self.age)
        idade=None
        if int(x) == 1:
            idade = 10
        elif int(x) == 2:
            idade = 25
        elif int(x) >2:
            idade = 25 + ((x-2)*4)

        self.real=idade


        return self.detail()

bichos = {"cachorro":Dog, "gato":Cat}

class Patas:
    __patinhas=4

    def andando(self):
        print(self.__patinhas)
        

def main():
    tipo=input("seu animal é cachorro ou gato?")
    name= input("insira o nome do seu {}:".format(tipo))
    color= input("qual a cor do seu {}:".format(tipo))
    ins_age=input("qual a idade do seu {}:".format(tipo))
    rem_age=[int(find) for find in ins_age.split() if find.isdigit()]
    age= rem_age[0]
    new_client = bichos.get(tipo, Animal)(name,color,age)
      
    print("======\n"+new_client.grito())

def test():
    x=Patas()
    x.__patinhas()
    print(x._Patas__patinhas)
   
if __name__ =="__main__":
    test()