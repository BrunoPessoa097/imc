'''
    Version: 1.0.0
'''

from tkinter import *
from index import main, apenasNumeros;

class Application:
    '''
        Criar todas as ligações entre o GUI e o back.
    '''

    def __init__(self, master=None):
        '''
            Cria a interfaze gráfica.
        '''

        # Definindo a fonte padrão como o tamanho.
        self.fontPadrao = ("Arial","10")

        # Cria um container.
        self.primeiroContainer = Frame(master)
        # Equivalente ao eixo y do CSS.
        self.primeiroContainer["pady"] = 10 
        # Exibe em tela.
        self.primeiroContainer.pack() 

        # Cria um container(mesmo padrão do 1 container, ver linha 23 e 25 caso dúvida).
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        # Cria um container(mesmo padrão do 1 container, ver linha 23 e 25 caso dúvida).
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        # Cria um container(mesmo padrão do 1 container, ver linha 23 e 25 caso dúvida).
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        # Cria um container(mesmo padrão do 1 container, ver linha 23 e 25 caso dúvida).
        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        # Cria no container o titulo da aplicação.
        self.titulo = Label(self.primeiroContainer, text="Calculo do IMC")
        # Seleciona a fonte, tamanho, e estilo.
        self.titulo["font"] = ("Arial","10","bold")
        self.titulo.pack()

        # Cria o label do peso container designado, texto do label e fonte.
        self.pesoLabel = Label(self.segundoContainer, text="Informe seu peso ", font=self.fontPadrao)
        self.pesoLabel.pack(side=LEFT)

        # Cria o input para o usuário no container designado.
        self.peso = Entry(self.segundoContainer)
        # Style do input como largura, fonte, e posicionamento.
        self.peso["width"] = 30
        self.peso["font"] = self.fontPadrao
        self.peso.pack(side=LEFT)

        # Cria o altura do peso container designado, texto do label e fonte.
        self.alturaLabel = Label(self.terceiroContainer, text="Informe sua altura", font=self.fontPadrao)
        self.alturaLabel.pack(side=LEFT)

        # Cria o input para o usuário no container designado.
        self.altura = Entry(self.terceiroContainer)
        # Style do input como largura, fonte, e posicionamento.
        self.altura["width"] = 30
        self.altura["font"] = self.fontPadrao
        self.altura.pack(side=LEFT)

        # Cria o butão calcular IMC
        self.autentificar = Button(self.quartoContainer)
        # Style do butão.
        self.autentificar["text"] = "Calcular"
        self.autentificar["font"] = ("Calibri","8")
        self.autentificar["width"] = 12
        # chama a função que o botão irá executar.
        self.autentificar["command"] = self.mostra
        self.autentificar.pack(side=LEFT)

        # Cria o botão limpar.
        self.limpar = Button(self.quartoContainer)
        # Style do botão.
        self.limpar["text"] = "Limpar"
        self.limpar["font"] = ("Calibri","8")
        self.limpar["width"] = 12
        # Chama a função que o butão irá executar.
        self.limpar["command"] = self.clear
        self.limpar.pack(side=LEFT,padx=5)

        # Cria o botão sair.
        self.sair = Button(self.quartoContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri","8")
        self.sair["width"] = 12
        # Finaliza o programa
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack(side=LEFT) 

        # Cria a mensagem de saida.
        self.mensagem = Label(self.quintoContainer, text="", font=self.fontPadrao)
        self.mensagem.pack()
        
    def clear(self):
        '''
            limpa as entradas e a saida do programa.
        '''
        self.peso.delete(0,END)
        self.altura.delete(0,END)
        self.mensagem["text"] = ""

    def mostra(self):
        '''
            realiza as operação de calculo, chamando as função para que o programa funciona.

            Args:
                self(class): Cria o GUI.
        '''

        # Captura as entradas do usuário.
        peso = self.peso.get()
        altura = self.altura.get()

        peso = apenasNumeros(peso)
        altura =apenasNumeros(altura)

        # Verifica se as entradas não estão vazias.
        if peso != "" and altura != "":
            self.mensagem["text"] = main(peso,altura);
        elif peso == "" or altura == "":
            self.mensagem["text"] = "Existe campo(s) vazio(s)"
        elif peso == ' ' or altura == ' ':
            self.mensagem["text"] = "erro";


# Executa o tinker, no qual e responsável pela parte gráfica. 
root = Tk()
root.title("IMC - Peso Corporal       versão 1.0.0")
Application(root)
root.mainloop()