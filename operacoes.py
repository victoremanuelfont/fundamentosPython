a = 2
b = 4
c = 6

#Operacoes matemáticas
print(a + b)
print(b - a)
print(c * b)
print(c / b)
print("__________________")

#operadores de comparacao
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= c)
print(a <= c)
print("__________________")

#operadores lógicos and, or, not
print(a == b and b < c)
print(a != b and b < c) #and se um for false a saída vai ser false
print(b > a or b >= c) #or basta um ser verdadeiro para a saída ser true
print(b < a or c > b)
print(not (a == c)) # not inverte o valor
print(not (b <= a or b > c))
print("__________________")


print(c % b) #resto da divisão
print(a ** b) #Exponeciação
print(c // b) #divisão inteira, descarta a parte decimal 
print("__________________")


#Expressoes aritméticas
print( a + b * c)  #Multiplicação primeiro
print ((a + b)* c) #primeiro dentro do parentese 
print("__________________")

#Expressoes matemáticas
a = 5
b = 3
c = 2
d = 10

expressao_matematica = (a + b) * (c - d) / (a ** c)
print(f"Expressão Matemática: {expressao_matematica}")

# Equação grande
equacao_grande = ((a + b) * (c - d) / (a ** c)) + (d / (a + c) - b * c)
print(f"Equação Grande: {equacao_grande}") 

# Expressões Condicionais Complexas
# Combinando operadores lógicos e de comparação

# Definindo variáveis
x = 8
y = 12
z = 20

# Expressão complexa com operadores condicionais
expressao_condicional = (x > y and y < z) or (x + y > z and not (z == x * 2))
print(f"Expressão Condicional: {expressao_condicional}") 

# Outra expressão complexa
outra_expressao_condicional = (x < y and y == z) or (x + z > y and not (x == z / 2))
print(f"Outra Expressão Condicional: {outra_expressao_condicional}") 

# Expressões Relacionais Complexas
# Combinando operadores matemáticos, lógicos e de comparação

# Definindo variáveis
m = 15
n = 25
p = 35

# Expressão complexa combinando diferentes operadores
expressao_relacional = ((m * n) > (p + m)) and ((p / n) < m) or not (p == m + n)
print(f"Expressão Relacional: {expressao_relacional}") 

# Outra expressão relacional complexa
outra_expressao_relacional = ((m + n - p) * (p / m) > n) and ((m ** 2) < p) or (n != m + p)
print(f"Outra Expressão Relacional: {outra_expressao_relacional}") 







