frase = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em letras maiusculas é: {frase.upper()}')

print(f'Seu nome em letras minusculas é: {frase.lower()}')

# frase_ = frase.replace(' ','')#metodo GPT
# print(f'Seu nome tem {len(frase_)} letras')#metodo GPT
print(f'Seu nome tem {len(frase) - frase.count(" ")} letras')#metodo Guanabara

# fr = frase.split()[0]#GPT
# print(f'Seu primeiro nomme tem {len(fr)} letras')#GPT
print(f'Seu primeiro nome tem {frase.find(" ")} letras')#Guanabara