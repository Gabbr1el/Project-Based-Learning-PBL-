import random
import sys

player1 = ''
player2 = ''

player_1_score = 0
player_2_score = 0

text = []
option = ''
termlist = []
round_size = -1

tentative = 1
atual_rounds = 1
rounds_totality = 0

player_atuality = ''

atual_points = []

MAX_TERMO_WORD_LENGTH = 5
COLOR_RED = '\033[31m'
COLOR_YELLOW = '\033[33m'
COLOR_GREEN = '\033[32m'
COLOR_RESET = '\033[0m'
COLOR_CIAN = '\033[36m'

def main():
    start()

def start():
    global option
    while option != '1' and option != '2':
        TelaGame()
        option = str(input('INSIRA SUA OPÇÃO: '))
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
       
        if option != '1' and option != '2':
            print(f'\n{COLOR_RED}OPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. {COLOR_RESET}')
            
    if option == '1':
        TelaGame1()
    elif option == '2':
        finish()

def TelaGame():
    print('----------------------------------------')
    print('| GAME: TERMO                          |')
    print('| DESENVOLVIDO POR: Felipe Gabriel     |')
    print('|                                      |')
    print('| Selecione:                           |')
    print('|                                      |')
    print(f'|{COLOR_GREEN} 1 - NOVO JOGO                        {COLOR_RESET}|')
    print(f'|{COLOR_RED} 2 - SAIR                             {COLOR_RESET}|')
    print('----------------------------------------\n')

def GameEspecification():
    print('----------------------------------------')
    print(f'|{COLOR_CIAN} TERMO:                   NOVO JOGO:{COLOR_RESET}  | ')
    print('----------------------------------------\n')



def TelaGame1():
    GameEspecification()
    global atual_rounds
    global player_atuality
    global player1
    global player2
    global text
    global rounds_totality
    
    print(f'{COLOR_RED}O NOME DO JOGADOR 1 NÃO PODE SER IGUAL AO DO JOGADOR 2, ASSIM COMO AO INVERSO!\n{COLOR_RESET}')
    
    player1 = str(input('ADICIONE O NOME DO JOGADOR 1: '))
    print('')
    player2 = str(input('ADICIONE O NOME DO JOGADOR 2: '))
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    
    while player1 == '' or player2 == '' or player1 == player2:
      print(f'\n\n\n\n\n{COLOR_RED}OPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. {COLOR_RESET}')
      player1 = str(input('ADICIONE O NOME DO JOGADOR 1: '))
      print('')
      player2 = str(input('ADICIONE O NOME DO JOGADOR 2: '))    
      print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')   
      
        
      
    GameEspecification()
    text = str(input('DIGITE ALGUM TEXTO ALEATÓRIO PARA O DICIONÁRIO (Obs: as palavras devem conter 5 letras, e pode ser espaçada do jeito que você quiser): ')).upper()
    while text == '' or len(text)< 5:
        print(f'{COLOR_RED}OPÇÃO SELECIONADA É INVÁLIDA, DIGITE NOVAMENTE. {COLOR_RESET}')
        text = str(input('\n\nDIGITE ALGUM TEXTO ALEATÓRIO AO DICIONÁRIO: ')).upper()
        if text != '' and len(text) > 5:
          break
    filter(text)
    
    
    while True:
        print(f'\nValor Máximo: {len(termlist)}')
        rounds_totality = int(input("Defina a quantidade de rodadas: "))
        if rounds_totality > len(termlist):
            print(f'{COLOR_RED}\nOPS! A QUANTIDADE DE ROUNDS ULTRAPASSA A QUANTIDADE DE PALAVRAS NA LISTA DE PALAVRAS DO TERMO... POR FAVOR DIGITE UM VALOR MENOR!{COLOR_RESET}')
        elif rounds_totality == 0:
            print(f'\n{COLOR_RED}VOCÊ PROVAVELMENTE NÃO ADICIONOU NENHUM ITEM AO DICIONÁRIO OU SEU DICIONÁRIO NÃO TEM NENHUMA PALAVRA COM 5 LETRAS... REPITA O PROCESSO{COLOR_RESET}')
        elif rounds_totality <= len(termlist):
            break
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    TelaGame2()


def TelaGame2():
    user_words = []
    
    global termlist
    global atual_rounds
    global tentative
    global rounds_totality
    global player_1_score
    global player_2_score

    def checagem5letras():
        if len(palavra) < 5:
            print("Erro, sua palavra tem menos de 5 letras!")
            TelaGame2()
        elif len(palavra) > 5:
            print("Erro, sua palavra tem mais de 5 letras!")
            TelaGame2()
    for round in range(1, rounds_totality + 1):
        pontuation = 120
        round_index = random.randint(0, len(termlist) - 1)  #index gerado randomicamente
        for tentative in range(1,7):
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('GAME: TERMO                                      ')
            print('')
            print(f'Rodada: {atual_rounds}         Rodadas Totais: {rounds_totality}         Tentativa: {tentative}         jogador: {player1 if round % 2 != 0 else player2}')
            showTermoWordList(user_words, termlist[round_index])
            print('[ ] [ ] [ ] [ ] [ ]')
            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
            palavra = (input(str('Adicione uma palavra: ')).upper())
            checagem5letras()
            user_words.append(palavra)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            
            if user_words[-1] != termlist[round_index]:
                pontuation -= 20
            else:
                if round % 2 !=0:
                    player_1_score += pontuation
                else:
                    player_2_score += pontuation

                print(f'\n\n{COLOR_GREEN}Parabéns voce conseguiu !{COLOR_RESET}')
                user_words = []
                

            if pontuation == 0:
                print(f'\n\n {COLOR_RED}Ops! parece que voce perdeu!{COLOR_RESET}')
                user_words = []
                
        termlist.pop(round_index)
    print(f'jogador: {player1} pontuação: {player_1_score}')
    print(f'jogador: {player2} pontuação: {player_2_score}')


def showTermoWordList (text, termo_word):
    global COLOR_GREEN
    global COLOR_RED
    global COLOR_RESET
    global COLOR_YELLOW


    for user_word in text:

        word_to_show = ''
        user_word_letter_list = list(str(user_word))
        termo_word_letter_list = list(str(termo_word))
        contains_letter_in_word_list = []
        for index in range(0, MAX_TERMO_WORD_LENGTH):

            contains_letter = user_word_letter_list[index] in termo_word and (user_word_letter_list[index] in contains_letter_in_word_list) == False
            is_letter = user_word_letter_list[index] == termo_word_letter_list[index]
         
            if contains_letter:
                contains_letter_in_word_list.append(user_word_letter_list[index])
                
            

            if is_letter:
                word_to_show += f'[{COLOR_GREEN}{user_word_letter_list[index]}{COLOR_RESET}] '
            elif contains_letter:
                word_to_show += f'[{COLOR_YELLOW}{user_word_letter_list[index]}{COLOR_RESET}] '
            else:
                word_to_show += f'[{user_word_letter_list[index]}] '
        print(f'{word_to_show}{COLOR_RESET}')
                            
                

def filter(text):
  wordslist = text.split(' ')
  for words in wordslist:
      words = words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', '')
      if len(words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', '')) == 5:
          global termlist
          if words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', '') not in termlist:
              termlist.append(words.replace(',', '').replace('.', '').replace('!', '').replace('@', '').replace('(', '').replace(')', '').replace('?', ''))
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def finish():
    print('\033[32mMUITO OBRIGADO POR JOGAR!!! \n\n\n\n\n\n\n\033[0;0m')
    
    sys.exit()

def reload():
    start()