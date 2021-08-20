class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def __add__(self, new_value):
        return Juice(self.name +"&"+ new_value.name, self.capacity + new_value.capacity)



def main():
    fruit1= Juice("Orange", 1.5)
    fruit2= Juice("Apple", 2.0)

    result = fruit1 + fruit2
    print(result.name + " (" + str(result.capacity) + "L)")


if __name__ =="__main__":
    main()