﻿# problem adding path in packaged version, use normal module instead
import sys;

sys.path.insert(0, '.');
sys.path.insert(0, './engine')
from console import Console
from logic import Parser

STORYBOARD_PATH = 'storyboard.yaml'


def title():
    Console.writeln("""  _   _            _""")
    Console.writeln(""" | | | | __ _ _ __| | _____ _ __""")
    Console.writeln(""" | |_| |/ _` | '__| |/ / _ \ '__|""")
    Console.writeln(""" |  _  | (_| | |  |   <  __/ |""")
    Console.writeln(""" |_| |_|\__,_|_|  |_|\_\___|_|""")
    Console.writeln('\n 2018 - Hermes Passer, baseado em Dracula de Bram Stoker')
    Console.writeln('site: hermespasser.github.io | código: github.com/hermespasser/harker')
    Console.writeln("\nDigite 'iniciar' para começar o jogo ou 'ajuda' para outras ações.")
    Console.writeln("Ao clicar com o mouse o jogo pode ser pausado, tecle enter para ele voltar.")


def main():
    title()
    while (True):
        arg = Console.scan_args() or 1
        if arg == 1:
            continue
        arg = arg[0]

        if (arg == 'iniciar'):
            Console.scroll_down()
            Parser(STORYBOARD_PATH).start()
            break
        elif (arg == 'carregar'):
            parser = Parser(STORYBOARD_PATH)
            parser.load()
            parser.start()
        elif (arg == 'ajuda'):
            Console.writeln("iniciar, carregar, encerrar")
        elif (arg == 'encerrar'):
            break
        else:
            Console.writeln("Comando inválido '%s'. Escreva 'ajuda' para ver as ações." % arg)


if (__name__ == "__main__"):
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        sys.exit(1)
