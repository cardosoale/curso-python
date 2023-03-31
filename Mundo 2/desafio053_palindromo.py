def eh_palindromo(s):
    s = s.replace(' ', '')
    return s == s[:: -1]

texto = input('Digite um texto: ')
if eh_palindromo(texto):
    print('O texto é um palíndromo.')
else:
    print('O texto não é um palíndromo.')