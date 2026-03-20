#Lista mas que armazena varios dados tipados

sensor = {"id": 1, "tipo": "temperatura"}
print(sensor["id"])
print(sensor["tipo"])
print("___________________")

#Alterando o dicionario
sensor["id"] = 2
print(sensor["id"])

#Imprimir todo o dicionario
print(sensor)
print("___________________")

#Operaçoes com dicionarios
estados_maquinas = {
    "maquina_1": "operacional",
    "maquina_2": "manutencao",
    "maquina_3": "parada"
}

print(estados_maquinas)
print("___________________")

#Adicionando novos estados ao dicionarios
estados_maquinas.update({"maquina_4": "operacional"})
print(estados_maquinas)
print("___________________")

#Acessando estados especi´ficos
print(estados_maquinas["maquina_3"])
print("___________________")

#Alterando 
estados_maquinas["maquina_3"] = "Operacional"
print(estados_maquinas)
print("___________________")

#Removendo um estado
del estados_maquinas["maquina_3"] 
print(estados_maquinas)
print("___________________")

#Listando todas as máquinas cadastradas/ lista os indices
print(estados_maquinas.keys())
print("___________________")

#Definindo um dicionário dentro do dicionário
comandos_maquinas = {
    "maquina_A": ["ligar", "monitorar", "desligar"], 
    "maquina_B": ["manutencao", "calibrar"], 
    "maquina_C": ["CHORO", "DESESPERO"]
}

print(comandos_maquinas)
print("___________________")

#Acessando o indice
print(comandos_maquinas["maquina_A"].pop(0))
print("___________________")

print(comandos_maquinas)
print(len(comandos_maquinas))