
print('Seja bem vindo ao quiz do Erick!')

quer = str(input('Quer começar? [S/N]:'))
while quer != 'S' and quer != 'N':
       print('Apenas  [S/N]')
       quer = str(input('Quer continuar [S/N]:'))


       score = 0

       print('Começando...')
       print('''Quem criou o jogo GTA V? 
         [A] Rockstar Games
         [B] EA  
         [C] Ubisoft 
         [D] Nenhuma dessas ''')
       resp = str(input('qual sua resposta?')).lower()
       if resp in 'aA':
            print('\033[36mCorreto..\033[m')
            score+=1
       else:
            print('\033[31mErrado, tem mais sorte na proxima\033[m'
                  '\nA Resposta É [A] Rockstar Games\033[m')
       print()

       print('''Qual nome do filho do michael? 
          [A] Carl Johnson
          [B] Trevor  
          [C] Jimmy 
          [D] Nenhuma dessas ''')
       resp1 = str(input('qual sua resposta?')).lower()
       if resp1 in 'Cc':
            print('\033[36mCorreto..\033[m')
            score+=1
       else:
            print('\033[31mErrado, tem mais sorte na proxima\033[m'
                  '\nA Resposta  certa é [C] jimmy\033[m')


       print(f'Quiz acabou.... sua pontuação foi {score}/2')

