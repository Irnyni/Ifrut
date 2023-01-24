def limpar():
    # Importando o módulo do sistema operacional (os) para usar instruções dele
    import os
    # Importando o módulo time para utilizar o método sleep que aguarda o 
    # tempo em segundos informando dentro do parênteses
    from time import sleep
    
    # Função para limpar a tela
    def screen_clear():
    # Para os sistemas operacionais: mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Para o sistema operacional windows
            _ = os.system('cls')
    # Aguarda 1 segundo para executar a próxima instrução
    sleep(1)
    # Chama a função de limpeza
    screen_clear()