#Declaração de variáveis

#inteiro
contagem_eventos = 150

#float
sensor_temperatura = 25.5

#string
nome_dispositivo = "SensorX100"

#Booleano
status_operacional = True

#Número complexo 
numnero_complexo = 3 + 4j

# Erros comuns
# Nome de variável não pode começar com número
# 1numero = 10 

# Nome de variável não pode conter caracteres especiais
# @sensor = 20

# 'for' é uma palavra reservada
# for = 30

# As variáveis têm o mesmo nome, porém, o Python interpreta que são
# variáveis diferentes devido ao uso de maiúsculas e minúsculas
sensor_temperatura = 28 # Variável com todas as letras minúsculas
Sensor_temperatura = 32 # Variável com a primeira letra maiúscula

#Conversão de variáveis

#String parta Inteiro
numero_str = "100"
numero_int = int(numero_str)
print (numero_int) #sai´da: 100

#String para float
numero_str = "100.5"
numero_float = float(numero_str)
print(numero_float) #saida: 100.5

#Inteiro para string
numero_int = 100
numero_str = str(numero_int)
print(numero_str)

#Conversão de string para booleano
boolean_str = "True"
boolean_val = bool(boolean_str) #Converte a string "True" patra um booleano True
print(boolean_val) #Saída: True

#Conversão de inteiro para booleano
boolean_int = 1 
boolean_val = bool(boolean_int)
print(boolean_val) # a saída vai ser true porque o int é 1, se fosse 0 a saída é false

#Conversão de float para booleano
numero_float = 0.0
boolean_val = bool(numero_float) #Qualquer numero diferente de ZERO é true. 0.0=0=false
print(boolean_val)

# Conversão de booleano para string
boolean_val = True
boolean_str = str(boolean_val) # Converte o booleano True para uma string "True"
print(boolean_str) # Saída: "True"