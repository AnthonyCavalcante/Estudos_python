celsius=int(input("insira um valor: "))

def conv(x):
    res=((9/5)*x+32)
    return res 

fahrenheit= conv(celsius)
print(fahrenheit)