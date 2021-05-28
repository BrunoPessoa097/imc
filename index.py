# Repete a execução do programa.
retornar = True
# Seleciona se o modo desenvolvedor esta ligado.
shell = True

def imc(peso,altura):
    '''
        Calcula o IMC corporal do individuo.

        Args:
            peso(float): peso da individuo.
            altura(float): peso da individuo.

        Return:
            calculo do IMC.
    '''
    return  peso / (altura * altura)

def tipologia(resultado):
    '''
        Retorna se o individuo está com sobrepeso ou não.

        Args:
            resultado(float): resultado do calculo do IMC.

        Return:
            retorno uma frase se a pessoa está com o peso ideal(frase).
    '''

    if resultado <= 18.5:
        return "Magreza - obesidade tipo 0"
    elif resultado > 18.5 or resultado <= 24.9:
        return "Normal - Obesidade tipo 0"
    elif resultado >= 25 or resultado <= 29.9:
        return "Sobrepeso - Obesidade tipo 1"
    elif resultado > 29.9 or resultado <= 39.9:
        return "Obesidade - Obesidade tipo 2"
    else:
        return "Obesidade grave - Obesidade tipo 3"

