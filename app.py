import webbrowser
import pyautogui
from time import sleep

def logout():
    pyautogui.click(x=-43, y=-62, duration=1)
    sleep(1)
    pyautogui.click(x=-1235, y=824, duration=1)
    sleep(1)
    pyautogui.click(x=-1208, y=761, duration=1)

while True:
    # 1 - Navegar até o site: https://www.instagram.com
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(5)
    # 2 - Entrar com usuário/email
    pyautogui.click(x=-462, y=198, duration=1)
    pyautogui.typewrite('mathias.sammer.946@gmail.com')
    sleep(1)
    # 3 - Entrar com senha do usuário
    pyautogui.press('tab')
    pyautogui.typewrite('InstAgrAm@19970925')
    sleep(1)
    # 4 - Clicar no botão "Entrar"
    pyautogui.click(x=-445, y=292, duration=1)
    sleep(10)
    # 5 - Clicar em "Agora não" para não salvar navegador
    pyautogui.click(x=-523, y=439, duration=1)
    sleep(3)
    # 5.1 - Clicar em "Agora não" para não ativar notificações
    pyautogui.click(x=-648, y=538, duration=1)
    sleep(1)
    # 6 - Clicar na aba de pesquisar
    pyautogui.click(x=-1183, y=96, duration=1)
    sleep(1)
    # 7 - Escrever o perfil desejado na busca
    pyautogui.typewrite('nike')
    sleep(5)
    # 8 - Clicar no perfil para acessar
    pyautogui.click(x=-1111, y=107, duration=1)
    sleep(10)
    # 9 - Clicar na postagem mais recente
    pyautogui.click(x=-839, y=573, duration=1)
    sleep(10)
    # 10 - Verificar se já foi curtido ou não aquela postagem
    like = pyautogui.locateCenterOnScreen('like.png')
    sleep(1)
    # 11 - Se já tiver curtido, fazer nada e pausar o bot por 24h
    if like is not None:
        # Sair da conta
        logout()
        sleep(86400)
    # 12 - Caso contrário, se não tiver curtido, curtir a foto
    elif like == None:
        pyautogui.click(x=-612, y=723, duration=1)
        sleep(5)
        pyautogui.click(x=-573, y=722, duration=1)
        sleep(3)
        # 13 - comentar na foto
        pyautogui.typewrite('Gostei dessa vídeo!')
        sleep(3)
        pyautogui.click(x=-181, y=824, duration=1)
        sleep(3)
        # Sair da conta
        logout()
        # 14 - Pausar por 24 horas
        sleep(86400)