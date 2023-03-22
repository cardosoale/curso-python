fr = 'corinthians campeão'
print(fr[12:19])
print(fr[12:])
print(fr[12::2])
print(fr[:5])
print(len(fr))#comprimento
print(fr.count('o'))# quantas letras o
print(fr.find('th'))#pos inicial
print(('corinthians' in fr))

#imprimindo textos longos
print("""\nMeu desejo? era ser o teu espelho
Que mais bela te vê quando deslaças
Do baile as roupas de escomilha e flores
E mira-te amoroso as nuas graças!\n""")

print(fr.replace('corinthians', 'timão').upper())

fr = fr.replace('corinthians', 'timão').upper()
print(fr)

div = fr.split()
print(div)
print(div[1][3])

