from functions.webfind import find_products
import json
import time
#entrar no ecommerce
#pesquisar produto
#capturar informação do produto pesquisado (nome, preco, site de pesquisa)
#guardar informações numa planilha
#rodar tudo em mais de 1 ecommerce (americanas - magazineluiza - amazon - casasbahia)
with open('docs\\urls_e_ids.json') as f:
    read_json = f.read()
url = json.loads(read_json)

def main():
   time.sleep(3)
   product = input("qual produto você quer pesquisar:\n")
   

   site = url.get("google")[0]
   get_id= url.get("google")[1]
   find_products(site, get_id, product)

   




if __name__ == '__main__':
    main()
    