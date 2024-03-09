from colorama import init, Fore, Back

init()

print(Fore.RED + 'Цей текст червоний.')
print(Fore.GREEN + 'Цей текст зелений.')
print(Back.YELLOW + 'Цей текст має жовтий фон.')

print(Fore.RESET + Back.RESET + 'Цей текст має стандартний колір тексту та фону.')
