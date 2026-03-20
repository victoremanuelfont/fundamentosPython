
#Uso do Loop for
for i in range(10):
    print("Produto", i+1, "verificado")

print("-----------------------------")


ordem = ["arroz","feijão","macarrão", "bife"]
for x in ordem:
    print("O prato é: ", x)
print("-----------------------------")


#Loop while: precisa ter uma condição de parada se não fica infinito
temperatura = 20
while temperatura <=25:
    print(f"Temperatura: {temperatura:.2f}°C")
    temperatura +=1
print("-----------------------------")

#Fluxos Iterativos e Laços de Repetição

# Importando a biblioteca necessária para simular o tempo
import time

# Definindo o consumo de energia inicial
consumo_energia = 50  # Consumo inicial em kW
limite_superior = 100  # Limite superior de consumo seguro em kW

# Laço de repetição para monitorar o consumo de energia
while True:  
    print(f"Consumo de energia atual: {consumo_energia} kW")  
    if consumo_energia > limite_superior:
        print("Alerta: Consumo de energia acima do limite seguro!")
        break  # Sai do loop se o limite for ultrapassado

    # Simulando a variação do consumo de energia
    consumo_energia += 10  # Aumenta o consumo em 10 kW
    #time.sleep(2)  # Pausa de 2 segundos entre as leituras

print("Monitoramento encerrado.")
print("-----------------------------")


#Loop for: Iterando com range(), lista e dicionário

for ciclo in range(1,6): #vai do 1 ao 6
    consumo = 50 + ciclo*8
    print(f"Ciclo {ciclo}: Consumo de energia = {consumo}kw")
print("-----------------------------")

for ciclo in range(1,10,2): #Vai de 1 a 10 pulando dois em dois
    print(ciclo)
print("-----------------------------")

#Usando for e listas
leituras = [55, 63, 70, 95, 105]
for leitura in leituras:
    if leitura > 100:
        print(f"Alerta! Consumo de {leitura} kw excedeu o limite!")
    else:
        print(f"Consumo dentro do limites:{leitura}kw")
print("-----------------------------")

#Usando for com dicionário
consumo_setores = {
    "Produção": 88,
    "Refrigeração": 102,
    "Iluminação": 76
}

for setor, consumo in consumo_setores.items():
    if consumo > 100:
        status = "Acima do limite"
    else:
        status = "Dentro do limite"

    print(f"Setor: {setor} | Consumo: {consumo}kw - Status: {status}")
