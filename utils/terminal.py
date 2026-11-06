import os


def clear_terminal():

    os.system('cls' if os.name == 'nt' else 'clear')


def pause_terminal():

    input("\nAppuyez sur Enter pour continuer...")