import os
import sys
import bs4

src = os.path.join(os.path.dirname(os.getcwd()))
sys.path.append(src)

# from src import distutils
import requests


# from IPython.display import display
def cotacao_dolar():
    dolar = 'https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do'
    response = requests.get(dolar)
    taxa_compra = 0
    taxa_venda = 0

    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    table_dolar = soup.find_all('tr', class_="fundoPadraoBClaro2")
    t = 0
    for x in table_dolar:
        lista = x.find_all('td', align='right')
        for i in lista:
            if t == 0:
                taxa_compra = str(i.next_element)
                t += 1
            else:
                taxa_venda = str(i.next_element)

    taxa_compra = taxa_compra[:1] + '.' + taxa_compra[2:]
    taxa_venda = taxa_venda[:1] + '.' + taxa_venda[2:]
    print(f'Taxa de Compra {taxa_compra} \n Taxa de Venda {taxa_venda}')

    return taxa_compra, taxa_venda


cot = cotacao_dolar()
valor = float(input('Digite o valor é R$: '))
total = valor / float(cot[0])

print(f'Com {valor} é possível comprar {total} dólares')

# Para testar se a página está UP use => print(response) se a resposta for <Response [200]>, então OK.

# Analisando o Header

"""
print('Status Code:', response.status_code, '\n', response.reason, '\n')
print('Cabeçalho(Header): ', response.headers,'\n')
print('Tipo de Arquivo: ', response.headers['Content-Type'], '\n')
print('Tamanho do Arquivo: ', response.headers['Content-Length'],'\n')
"""

"""
Arquivos

file = open('dolar.html', 'wb+')
file.write(response.content)
file = open('dolar.html','r').read()
#f1 = file.readlines()
print(file)
"""
