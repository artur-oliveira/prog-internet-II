from requests import get

response = get('https://www.cheapshark.com/api/1.0/deals')

for item in response.json():
    print('Nome do jogo: %s' % item.get('title'))
    print('Preço normal: %s' % item.get('normalPrice'))
    print('Preço atual: %s' % item.get('salePrice'))
    print('Desconto: U$$ %.0f %%' % float(item.get('savings')))
    print()
