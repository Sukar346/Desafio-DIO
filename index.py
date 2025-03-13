nome = input(str('Qual é o nome do seu Herói: '))
print(f'Seja bem vindo {nome}!')

xp = int(input('Quanto de experiência você tem?: '))

if xp <= 1000:
    print(f'"O Herói de nome **{nome}** está no nível de xp **{xp} o que equivale a patente Ferro**"')
    
elif 1001 <= xp <= 2000:
    print(f"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Bronze**")

elif 2001 <= xp <= 5000:
    print(f'"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Prata**"')

elif 5001 <= xp <= 7000:
    print(f'"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Ouro**"')

elif 7001 <= xp <= 8000:
    print(f'"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Platina**"')    

elif 8001 <= xp <= 9000:
    print(f'"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Ascendente**"')    

elif 9001 <= xp <= 10000:
    print(f'"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Imortal**"')    

elif xp >= 10001:
    print(f'"O Herói de nome **{nome}** está no nível de **{xp} o que equivale a patente Radiante**"')    