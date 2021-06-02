# IMC
<p align="center">Calcule a massa corporal</p>


<p align="center">

<img alt="autor" src="https://img.shields.io/badge/Autor-Bruno%20Pessoa-blue">
 
<img alt="python versão" src="https://img.shields.io/badge/Python- 3.9.5 -blue">

<img alt="versão projeto" src="https://img.shields.io/badge/Versão- 1.0.0 -blue">

<img alt="situação" src="https://img.shields.io/badge/Situação-Em Desenvolvimento -blue">

</p>

# Objetivo
Aprender uma linguagem, além de usar conhecimento já adquiridos anteriormente nesse projeto, bem como evoluir nos vários aspectos adquiridos com o projeto.
# Conteúdo
* [Descrição](#Descrição)
* [Dependência](#Dependência)
* [Executando o programa](#Executando-o-programa)
    * [Rodando pelo terminal](##Rodando-pelo-terminal)
        * [Editando o código](###Editando_o_código)
        * [Automático](###Editando_o_código)
    * [Parte gráfica](##Rodando-a-parte-gráfica(GUI))
        * [Escolhendo o arquivo](###Escolhendo_o_arquivo)
        * [Automático](###Automático)
* [Tecnologia](#Tecnologia)

# Descrição
Uma calculadora simples afim de saber seu IMC, bem como baseado na tabela do IMC como se encontra sua massa corporal.

# Dependência
Precisa ter instalado o [python](https://www.python.org/), e instalado a biblioteca python [PySimpleGUI](https://pypi.org/project/PySimpleGUI/).

# Executando o programa
Escolha como executar o programa, seja sem a parte gráfica somente pelo interpretador python ([terminal](##Rodando-pelo-terminal)), ou com a parte gráfica([GUI](##Rodando-a-parte-gráfica(GUI)))

## Rodando pelo terminal
Existe duas maneiras de executar pelo terminal logo abaixo ensina como faze-las, ficando a sua escolha.

### Editando o código.
1. Abra o arquivo `index.py`, toque o valor da variável shell que se encontra no inicio do código:

- Como estar.
``` python
    shell = False
```
- Para o valor abaixo
``` python
    shell = True
```
2. Após a mudança execute o arquivo `index.py`.
### Automático
1. Execute o arquivo `index.py`.
2. Aparecerá a pergunta abaixo:
``` console
    Deseja habilitar o terminal? y/n
```
3. Digite `y` - yes (sim) e o programa executará pelo terminal.


## Rodando a parte gráfica(GUI)
Existe 2 maneiras de rodar à parte gráfica.

### Escolhendo o arquivo.
Existe nessa verão(1.0.0) existem 2(dois) interfaces(GUI) nesse projeto, um com o tkinter, no qual é o arquivo `style.py`, e outro com PySimpleGUI, que é arquivo `simple.py`, independentemente da escolha, o processo é o mesmo para ambos, como mostrado abaixo:

1. Escolha o arquivo que deseja rodar `style.py` ou `simple.py`.
2. Execute o arquivo escolhido.

### Automático.
1. Execute o arquivo `index.py`.
2. Aparecerá no terminal a seguinte pergunta.
``` smd
    Deseja habilitar o terminal? y/n
```
3. Digíte `n` para não.
4. Aparecerá no terminal outra pergunta.
``` cmd
    Qual GUI deseja usar? digite (t) para tkinter ou (s) simpleply:
```
5. Selecione a interface desejada.

<b>OBS.:</b> caso não aconteça o foi dito verificar a variável `shell`, no arquivo `index.py` caso a mesmo estiver recebendo `True` mude para `False`.

</br>

# Tecnologia
As seguintes tecnologias foram usadas:
- [Python](https://www.python.org/) - versão 3.9.5
- [Tkinter](https://docs.python.org/pt-br/3/library/tkinter.html) - versão 3.9.5

- [PySimpleGUI](https://pypi.org/project/PySimpleGUI/) - versão 4.43.0

# Autor
Bruno Pessoa