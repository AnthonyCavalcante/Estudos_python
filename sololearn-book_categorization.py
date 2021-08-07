with open("books.txt", "w") as writ:
    writ.write("Some book\nAnother book")

with open("books.txt") as ler:
   categ= ler.readlines()
   for tittle in categ:
       print(tittle[0]+str(len(tittle.rstrip()))) 