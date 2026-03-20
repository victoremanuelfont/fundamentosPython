#Estruturas Esquenciais
lista = [22.5,23,24]
print(lista)
lista.append(27.92)
print(lista)
print("-----------------")

#Lista com dados fixos
tupla = (65,96)
print(tupla)
print("-----------------")

#Operaçoes com listas
temp_celsius = [25.1, 25.2, 24.9, 26.0, 25.8]
print(f"Leituras iniciais de temperatura: {temp_celsius}")
print("-----------------")

#adicionando nova temperatura
temp_celsius.append(29)
print(f"Leituras adicionais de temperatura: {temp_celsius}")
print("-----------------")

#Acessando elementos específicos
primeira_da_lista = temp_celsius[0]
print(primeira_da_lista)
ultima_da_lista = temp_celsius[-1]
print(ultima_da_lista)
print("-----------------")

#Modificando pelo indice
print(temp_celsius)
print(temp_celsius[2])
temp_celsius[2] = 175
print(temp_celsius)
print(temp_celsius[2])
print("-----------------")

#Removendo uma leitura 
temp_celsius.pop(2)
print(temp_celsius)
print("-----------------")

#Verificando o tamanho da lista
print(len(temp_celsius))
print("-----------------")

#Verificando a existencia de um valor
if 25.2 in temp_celsius:
    print("Tem")
else:
    print("Não tem")

print("-----------------")

#Ordenando as leituras
temp_celsius.sort()
print(temp_celsius)
