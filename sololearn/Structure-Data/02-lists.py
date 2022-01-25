
def exercise1():
    data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
    ]
    room = sum(data[0]) + sum(data[1])
    eyes = {'brown': 0, 'blue': 1, 'green': 2, 'black': 3}
    color = input()
    eyenumber = eyes.get(color)
    calculate = data[0][eyenumber] + data[1][eyenumber]
    percent_people = int((calculate/room)*100)
    print (percent_people)

def exercise2():
    prices = [125000, 78000, 110000, 65000, 300000, 250000, 210000, 150000, 
                165000, 140000, 125000, 85000, 90000,
                128000, 230000, 225000, 100000, 300000]
    soma = sum(prices)
    lenlist = len(prices)
    avg = soma/lenlist
    print(len([1 for _ in prices if _ > avg]))
    ''' m= []
    for house in prices:
        if house > avg:
            m.append(house)
    print (len(m))'''

def exercise3():
    ins = int(input())
    n = [ins*2**i for i in range(0,12)]
    print(n)

def avg_word():
    phrase = input()
    words = phrase.split()
    words_len = phrase.replace(' ','')
    avg_word = len(words_len) / len(words) 
    print (avg_word)



def main():
    exercise2()

if __name__ == '__main__':
   main()