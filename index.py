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

def run():
    '''
        Caso a individuo queira repetir o calculo, essa função só funciona no modo shell,
        e no terminal.

        Return:
            true ou false se a usuário deseja fazer ou refazer o calculo.
    '''
    escolha = input("Deseja continuar? y/n \n")

    if escolha == 'y':
        return True
    else:
        return False

def entrada(txt):
    '''
        Função generica para criar inputs do tipo float junto com o texto.

        Args:
            txt(str): o texto a ser colocado no input.

        Return:
            Input completo com texto e do tipo float.
    '''
    return float(input(txt))

def limpo(peso,altura):
    '''
        Verifica se recebeu alguma informação valida por parte do usuário.

        Args:
            peso(float): peso do usuário.
            altura(float): altura do usuário.

        Return:
            Verifica se as entradas(Args) dos usuários são válidas.
    '''

    if peso > 2.0:
        if altura > 0.45:
            return True
        else:
            return False
    else:
        return False

def imprimir(result):
    '''
        Imprimi a saída(resultado do IMC) para o usuário, feito para trabalhar com o GUI.

        Args:
            result(float): Resultado do IMC.

        Return:
            Frase com o IMC, junto com a informação sobre o seu condicionamento físico.
    '''
    return 'Seu IMC é: {:.2f}'.format(result)+"\n Você está: "+tipologia(result)

def main(peso=0,altura=0):
    '''
        Função principal que executa o necessário.

        Args:
            peso(float): peso informado pelo usuário.
            altura(float): altura informado pelo usuário.

        Return:
            Modo shell: o calculo do IMC como se o usuário deseja repetir a ação.
            Modo GUI: retorna o valor do IMC, junto com uma frase.
    '''

    # Modo desenvolvedor.
    if shell:
        global retornar
        
        altura = entrada("Informe sua altura: ")
        peso   = entrada("informe seu peso: ")

        if limpo(peso,altura):

            resultado = imc(peso,altura)

            print(tipologia(resultado))
            print("IMC: {:.2f}".format(resultado))
        
            retornar = run()
        else:
            main()
    # Modo GUI.
    else:
        retornar = False
        
        peso = float(peso)
        altura = float(altura)

        if peso or altura:
            calculo = imc(peso,altura)
            return imprimir(calculo)
        else:
            print("Habilite o Shell na linha 4")
        
# Define a função principal.
if __name__ == '__main__':
    while(retornar):
        main()
