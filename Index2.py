vitoria = int(input('Quantas vitórias você tem? : '))
derrota = int(input('Quantas derrotas você tem? : '))

def saldoVitorias(vitoria, derrota):
    return vitoria - derrota
saldoVitorias = vitoria - derrota
if saldoVitorias < 10:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Ferro")  

elif 11 >= saldoVitorias >= 20:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Bronze")       

elif 21 >= saldoVitorias >= 50:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Prata") 

elif 51 >= saldoVitorias >= 80:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Ouro")    

elif 81 >= saldoVitorias >= 90:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Diamante")      

elif 91 >= saldoVitorias >= 100:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Lendário")

elif saldoVitorias >= 101:
    print(f"O Herói tem de saldo de **{saldoVitorias}** está no nível de Imortal")                                
