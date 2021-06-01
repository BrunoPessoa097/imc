'''
    Version: 1.0.0
'''
import os
import re

# Repete a execução do programa.
retornar = True
# Seleciona se o modo desenvolvedor esta ligado.
shell = False

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
    escolha = input("Deseja continuar? y/n \n").lower()[0]

    if escolha == 'y':
        return True
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return False

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
    return 'Seu IMC é: {:.2f}'.format(result)+" Você está: "+tipologia(result)

def habilitar():
    '''
        Habilita automaticamente o terminal ou a interface sem a necessidade de abrir outro arquivo.
        
        Args:
            shell(boolean): Responsável por automatizar a execução do código no terimal, ou pelo GUI.
        
        Return:
            Oposto do que foi entrado de maneira booleana.    
    '''
    global shell

    if shell == False:
        shell = True
        main()
    else:
        shell = False

def apenasNumeros(txt):
    '''
        Remover dos dados informados tudo o que é números com exceção da virgula no qual converte para ponto.

        Attributes:
            alfabeto(sting): regExg do alfabeto.
            virgula(char): virgula.
            nada(string): caractere vazio.
            ponto(char): caractere de um ponto.

        Return:
            Um número decimal com 2(duas) casas decimais.
    '''
    alfabeto = '[A-Z a-z]'
    virgula= ','
    nada = ''
    ponto ='.'


    txt = re.sub(virgula,ponto,txt)
    txt = re.sub(alfabeto,nada,txt)
    
    return duasDecimal(txt)

def duasDecimal(txt):
    '''
        Decimal com 2(duas casas).

        Attributes:
            ponto(char): Caractere ponto.
        
        Return:
            Decimal com 2(duas) casas.
    '''
    ponto ='.'

    sucesso =  txt.find(ponto)

    if sucesso == -1:
        return txt
    else:
        return txt[0:sucesso+3]

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
        os.system('cls' if os.name == 'nt' else 'clear')

        global retornar
        
        altura = input("Informe sua altura: ")
        peso   = input("informe seu peso: ")
        
        altura = float(apenasNumeros(altura))
        peso = float(apenasNumeros(peso))

        if limpo(peso,altura):

            resultado = imc(peso,altura)

            print(tipologia(resultado))
            print("IMC: {:.2f}".format(resultado))
        
            retornar = run()
        else:
            main()
    # Modo GUI.
    else:
        os.system('cls')
        retornar = False
        
        if peso and altura:
            calculo = imc(peso,altura)
            return imprimir(calculo)
        else:
            saida = input("Deseja habilitar o terminal? y/n ").lower()[0];

            if saida == 'y':
                habilitar()  
            elif saida == 'n': 
                gui = input('Qual GUI deseja usar? digite (t) para tkinter ou (s) simpleply: ').lower()[0]

                if gui == 't':
                    os.system('python .\style.py')
                elif gui == 's':
                    os.system('python .\simple.py')
                else:
                    print('informe um valor válido')
                
            else:
                print('Informe uma entrada válida')
                main()

        
# Define a função principal.
if __name__ == '__main__':
    while(retornar):
        main()
