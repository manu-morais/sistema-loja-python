total = mais1000 = barato = cont = 0
nomebarato = ''
print('-'*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-'*40)
while True:
    nomep = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 0 or preco < barato:
        barato = preco
        nomebarato = nomep
    cont += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${barato:.2f}')