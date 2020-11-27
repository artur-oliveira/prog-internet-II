from requests import get

codigo_moeda = 'BRL'

response = get('https://api.exchangeratesapi.io/latest?base=%s' % codigo_moeda)

rates = response.json().get('rates')

print('EX:')
print('20 reais equivalem a %.2f dólares' % (20 * rates['USD']))
print('20 reais equivalem a %.2f euros' % (20 * rates['EUR']))

