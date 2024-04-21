def calcular_imc(peso, altura):
    altura_metros = altura / 100  # Converter altura para metros
    imc = peso / (altura_metros ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso Ideal (Para Bens)"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau 1"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"

def main():
    nome = input("Digite seu nome: ")
    altura = float(input("Digite sua altura em centímetros: "))
    peso = float(input("Digite seu peso em quilogramas: "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print("\nNome:", nome)
    print("Altura:", altura, "cm")
    print("Peso:", peso, "kg")
    print("IMC:", round(imc, 2))
    print("Classificação:", classificacao)

if __name__ == "__main__":
    main()
