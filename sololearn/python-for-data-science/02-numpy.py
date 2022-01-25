import numpy as np

def extra_numpy():
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
    z = np.arange(2,12,2)
    #m = z.reshape(3,2)
    re = x.reshape(9)
    print(x)
    print(re)

def exercise1():
    data = np.array([1000, 2500, 1400, 1800, 4200,900, 2200, 1900, 3500])
    new_house = int(input())
    data = np.append(data, new_house)
    data = np.sort(data)
    print(data)

def exercise2():
    data = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 0, 1, 0, 1,
                     1, 1, 1, 0, 0, 0, 1, 1, 1, 0])

    row = int(input())
    theater = data.reshape(int(len(data)/5),5)
    print(theater)
    print(theater[row])

def exercise3():
    data = np.arange(1,100) 
    print(data[(data%3==0) & (data%5==0)] )

def exercise4():
    data = np.array([120, 98, 150, 65, 42, 100, 190, 220, 140, 110, 88,
                     89, 100, 120, 50, 180, 155, 42, 89, 77, 200, 190, 
                     125, 98, 77, 40, 39, 59, 30, 67])
    print(len(data[(data>np.mean(data))]))

def house_prices():
    data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 
                        230000, 280000, 290000, 300000, 500000, 420000,
                         100000, 150000, 280000])
                         
    houses = data[(data > (np.mean(data) - np.std(data))) & (data <np.mean(data) + np.std(data))]
    print((data.size / houses.size)*100)


def main():
     house_prices()

if __name__ == '__main__':
    main()
    