palavras = ('gratis', 'python', 'casa', 'alexandre', 'curso', 'java', 'tenebroso', 'oreia')
for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
print('\n')