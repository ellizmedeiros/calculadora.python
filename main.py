# ============================================
# CALCULADORA SIMPLES EM PYTHON
# Operações: Adição, Subtração, Multiplicação, Divisão e Potência
# ============================================

# 1. Apresentação do programa
print("--- CALCULADORA SIMPLES ---")

# 2. Entrada do primeiro número
# O float() converte o texto digitado em número com vírgula/ponto
num1 = float(input("Digite o primeiro número: "))

# 3. Escolha da operação matemática
print("Escolha a operação:")
print("  + : Adição (Soma)")
print("  - : Subtração")
print("  * : Multiplicação")
print("  / : Divisão")
print("  ** ou ^ : Potência (Exponenciação)")
operacao = input("Digite o símbolo da operação (+, -, *, /, **): ")

# 4. Entrada do segundo número
num2 = float(input("Digite o segundo número: "))

# 5. Processamento e tomada de decisão (condicionais)
if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")

elif operacao == '/':
    # Regra importante da matemática: não existe divisão por zero!
    if num2 == 0:
        print("Erro: Não é possível dividir nenhum número por zero!")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")

elif operacao == '^' or operacao == '**':
    resultado = num1 ** num2
    print(f"Resultado: {num1} ** {num2} = {resultado}")

else:
    print("Erro: Operação inválida! Escolha +, -, *, / ou **")
