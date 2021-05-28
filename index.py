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

