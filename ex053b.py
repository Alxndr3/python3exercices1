'''frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
inverte = ''
for x in range(len(frase) -1, -1, -1):
    inverte += (frase[x])
if frase == inverte:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += (junto[letra])
if inverso == junto:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')





