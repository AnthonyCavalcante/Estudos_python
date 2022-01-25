#exercise 1
'''x = input('digite sua frase')
qtd = 0
vowel = ['a','e', 'i', 'o','u']

for letter in x:
    if letter in vowel:
        qtd += 1
print(qtd)'''

 #exercise 2
'''entrace = input()
for position,letter in enumerate(entrace):
    number = int(position + 1)
    result = letter*number
    print(result)'''

#exercise 3
'''text = "I weigh 80 kilograms. He weighs 65 kilograms."
findText = input()
changeText = input()

resultFind = text.count(findText)
newText = text.replace(findText, changeText)
print(resultFind)
print(newText)
'''
#test Letter Frequency
'''text = input()
letter = input()

lenText = len(text)
qtdletter = text.count(letter)
result = int((qtdletter/lenText)*100)

print (result)'''

l = 'testando'
s = set(l)
print (s)

