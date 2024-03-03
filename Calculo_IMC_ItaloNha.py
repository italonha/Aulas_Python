def main():
    peso = float(input('Qual é o seu peso? (Kg) '))
    altura = float(input('Qual é a sua altura? (m) '))
    imc = peso / (altura ** 2)
    print('O IMC dessa pessoa é de {}'.format(imc))
    
    if imc < 18.5:
        print('Você está ABAIXO DO PESO normal')
    elif 18.5 <= imc < 25:
        print('Parabéns, você está na faixa de PESO NORMAL')
    elif 25 <= imc < 40:
        print('Você está com SOBREPESO')

if __name__ == "__main__":
    main()