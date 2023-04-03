# def eh_palindromo(s):
#     s = s.replace(' ', '')
#     return s == s[:: -1]

# texto = input('Digite um texto: ')
# if eh_palindromo(texto):
#     print('O texto é um palíndromo.')
# else:
#     print('O texto não é um palíndromo.')

texto = input('Digite um texto: ').strip().upper()
palavras = texto.split()
junto = ''.join(palavras)
inverso = ''
# if junto == junto[::-1]:
#     print('PALÍNDROMO')
# else:
#     print('NÃO É PALÍNDROMO')

for letra in range(len(junto) -1, -1, -1):    
    inverso += junto[letra]
if junto == inverso:
    print(f'Esta frase "{texto}" é um PALÍNDROMO')
else:
    print(f'Esta frase "{texto}" não é um PALÍNDROMO')