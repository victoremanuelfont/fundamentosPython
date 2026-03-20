#exemplo de funcao
def informacao():
    print("Sistema de constrole de temperatura")
#chamando a funcao
informacao()
print("------------------------")

#exemplo de funcao para inicio de turno
def iniciar_turno():
    print("Início de turno")
    print("verifique")

iniciar_turno()
print("------------------------")

#exemplo usando parametros
def exibir_nome(nome):
    print(nome)

exibir_nome("VICTOR")
exibir_nome(nome = "victor")
nome = "ViCtOr"
exibir_nome(nome)
print("------------------------")

#Exemplo Retorno
def calcular_media(a,b):
    return (a+b)/2

print(calcular_media(1,9))
print("------------------------")


