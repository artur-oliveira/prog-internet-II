# Atividade 01 - Pesquisar Web API
As 3 APIs que eu procurei são as seguintes
- API de conversão de moedas
- API de encurtador de links
- API de promoções na Steam

## API conversão de moedas
Esta API serve para pegar taxas de câmbio entre as moedas do mundo <br><br>
Abaixo você pega as taxas de câmbio usando o Euro como base, é o padrão da API
```
GET https://api.exchangeratesapi.io/latest
```
Para trocar para reais, cuja sigla é BRL basta colocar o parâmetro base na url
```
GET https://api.exchangeratesapi.io/latest?base=BRL
```
Caso queira limitar as taxas de cambio, você pode colocar o parâmetro symbols
```
GET https://api.exchangeratesapi.io/latest?base=BRL&symbols=EUR,USD
```
Também é possível fazer a requisição de todas as taxas de câmbio entre um determinado período
```
GET https://api.exchangeratesapi.io/history?start_at=2018-01-01&end_at=2018-09-01
```

## API encurtador de links
Esta API serve para você encurtar links através do método POST <br> <br>
Abaixo você pode encurtar o link para o site do facebook por exemplo
```
curl -XPOST -d 'url=https%3A%2F%2Ffacebook.com%2F' 'https://cleanuri.com/api/v1/shorten'
```

## API promocoes steam
Esta API serve para pegar promoções camaradas na steam (Serve para outras coisas também, mas não achei útil) <br> <br>
Abaixo você pode pegar uma lista com todas as promoções
```
GET https://www.cheapshark.com/api/1.0/deals
```
