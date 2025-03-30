#Crear un programa que muestre cuantos BTC se podran minar 
#por cada halving que exista hasta un año limite dado por teclado

anio = float(input("Ingrese un año limite: "))
i = 2008
coin=50
btc = coin
while i <= anio:
    print("en el año " +str(i)+ " se minaran " +str(btc)+ " bitcoins por bloque")    
    i+=4
    btc/=2