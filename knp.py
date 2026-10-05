import random
moznosti = ["kamen", "nuzky", "papir"]
print("hra kamen,nuzky,papir")
print("Napiš 'q' pro konec. \n")
while True:
    pocitac = random.choice(moznosti)
    uzivatel = input('Zadej kamen / nuzky / papir: ').lower()
    if uzivatel == 'q':
        print('Diky za hru!')
        break
    if uzivatel not in moznosti:
        print('Neplatna volba. Zkus to znovu.')
        continue
    print(f'pocitac:{pocitac}')
    if uzivatel == pocitac:
        print('Remiza!')
    elif (uzivatel == 'kamen' and pocitac == 'nuzky') or (uzivatel == 'nuzky' and pocitac == 'papir') or (uzivatel == 'papir' and pocitac == 'kamen'):
        print('Vyhral jsi!')
    else:
        print('Vyhral pocitac!')
    print('-'*20)