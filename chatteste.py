import os

def processa_resposta(resposta,name):
    if resposta == "1":
        print(f"{os.linesep}{name} a linguagem javascript cresce a todo ano. Se você gosta de desenvolvimento web essa linguagem e uma boa pra começar.")
    elif resposta == "2":
        print(f"{os.linesep}{name}, essa linguagem python e uma linguagem bem versatil, você pode tanto trabalhar com analise de dados quanto automações e muito mais.")
    elif resposta == "3":
        print(f"{os.linesep}{name}, desenvolvimento web na pandemia teve uma crecente demanda de desenvolvedores mobile. E uma area também muito boa.")
    elif resposta == "4":
        print(f"{os.linesep}{name}, automação você pode estar automatizando qualquer tipo de tarefas repetitivas.")
    else:
        print(f"{os.linesep}{name}, digite apenas 1,2,3 ou 4")
        
def start():
    print("Ola seja bem vindo")
    name = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    while True:
        resposta = input(f"O que voce gostaria de saber hoje {name}:\n {os.linesep} [1] - Gostaria de apreender javascript?  {os.linesep} [2] - Gostaria de apreender Python? {os.linesep} [3] - Gostaria de apreender Desenvolvimento mobile? {os.linesep} [4] - Gostaria de apreender Automação? \n")
        processa_resposta(resposta,name)


if __name__ == '__main__':
    start()