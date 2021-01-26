#!/usr/bin/python3.8
import random as r
import os

numeros = '1234567890'
letras = 'abcdefghijklmnopqrstuvwxyz'
simbolos = '\'!|,.~^;+-=)(*&%$#@][}{><?/:\\_'
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
titulo = f"""{bcolors.OKBLUE}
░▒█▀▀█░█▀▀░█▀▀▄░█▀▀▄░█▀▄░▄▀▀▄░█▀▀▄░░░█▀▄░█▀▀░░░▒█▀▀▀█░█▀▀░█▀▀▄░█░░░░█▀▀▄░█▀▀
░▒█░▄▄░█▀▀░█▄▄▀░█▄▄█░█░█░█░░█░█▄▄▀░░░█░█░█▀▀░░░░▀▀▀▄▄░█▀▀░█░▒█░█▀▀█░█▄▄█░▀▀▄
░▒█▄▄▀░▀▀▀░▀░▀▀░▀░░▀░▀▀░░░▀▀░░▀░▀▀░░░▀▀░░▀▀▀░░░▒█▄▄▄█░▀▀▀░▀░░▀░▀░░▀░▀░░▀░▀▀▀
{bcolors.ENDC}"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generator(mai, sim, num, tamanho=18):
    s = str(letras)
    if sim:
        s += simbolos
    if num:
        s += numeros
    if mai:
        s += letras.upper()

    passwd = ''
    for i in range(tamanho):
        passwd += (s[r.randint(0, len(s)-1)])
    return f'\nsenha gerada > {bcolors.OKBLUE}{passwd}\n'


def menu():
    op = 0
    while op != 2:
        clear()
        print(titulo)
        print(f'\n{bcolors.HEADER}{bcolors.BOLD}*** Opcoes ***{bcolors.ENDC}\n-> Gerar senha (1)\n-> Sair (2)\n')
        try:
            op = int(input(f'{bcolors.ENDC}Entre com a opcao desejada > {bcolors.OKGREEN}{bcolors.BOLD}'))
        except:
            print(f'{bcolors.FAIL}\nentrada invalida :(\n{bcolors.ENDC}')
            return
        if op == 1:
            num = (True if input(f'{bcolors.ENDC}? incluir numeros ? (s, n) > {bcolors.OKGREEN}{bcolors.BOLD}') == 's' else False)
            mai = (True if input(f'{bcolors.ENDC}? incluir letras maiusculas ? (s, n) > {bcolors.OKGREEN}{bcolors.BOLD}') == 's' else False)
            sim = (True if input(f'{bcolors.ENDC}? incluir simbolos ? (s, n) > {bcolors.OKGREEN}{bcolors.BOLD}') == 's' else False)
            try:
                tam = int(input(f'{bcolors.ENDC}? Tamanho da senha ? (0-30) > {bcolors.OKGREEN}{bcolors.BOLD}'))
            except:
                print(f'{bcolors.FAIL}\nentrada invalida :(\n{bcolors.ENDC}')
                return
            if tam > 30:
                print(f'{bcolors.WARNING}\nsenha muito longa ;-;{bcolors.ENDC}')
                continue
            
            continua = False
            while continua is not True:
                print(generator(mai, sim, num, tam))
                continua = (True if input(f'{bcolors.ENDC}? gerar outra senha ? (s, n) > {bcolors.OKGREEN}') == 'n' else False)
            print(f'{bcolors.HEADER}\nate mais :)~\n')
            return
                
        elif op == 2:
            print(f'{bcolors.HEADER}\nate mais :)~\n')
            return
        else:
            print(f'{bcolors.FAIL}\nentrada invalida :(\n{bcolors.ENDC}')

menu()
