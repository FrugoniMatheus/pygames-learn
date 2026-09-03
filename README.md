# Firts Steps With Pygame

# Organização de pastas 

* Pasta  | Scripts
* Pasta  | Assets 
* Arquivo| Main.py

# Primeiros passos 

* Importar biblioteca de funções do pygame 

<code>import pygame<code>


## Setores

Tamanho, altura, escalonar ou não, alfa ou não 


pygame.init() - Da problema se for usar vídeo ou áudio - Tarefa muito importante

pygame.font.init() - Abrir a opções de textos
 -pygame.font.Font(None, 50) - None- sendo qual o estilho de tipografia e o 50 é o tamanho do texto
 -font.render("0", True, "white") - "0" - Insiro o texto que vai exibir, True - Se vai ter serrilhado ou não, "white"- se vai ter cor branca ou não.

pygame.display.set_mode((1280, 720)) - Tela pronta com as dimensões passadas, largura e altura.

display.blit(placar_player2, (780,50)) - Blit quer dizer vou desenhar algo, podendo ser na minha tela principal. placar_player = O que quero desenhar?; (780,50) onde ficará com posição x e y

fill() - Preenche a tela com uma determinada cor, dentro eu passo uma cor. 
(0,0,0) (vermelho, verde e azul)

pygame.display.flip() - Minha tela sempre vai ficar atualizando

pygame.event.get() - Lista de eventos que o pygame reconhece (mouse, teclado e controle)

pygame.QUIT - Botão de fechar a janela

pygame.KEYDOWN - Qualquer tecla pressionada (mouse, teclado ou controle)
 - pygame.K_x - Sendo x qualquer tecla que eu escolhe ele diz assim, se eu seleciona a tecla x o que acontece? 

pygame.Rect() - Formato de retanculo - Formato x, y ,largura e altura
 - .y = Alterar valor do eixo Y 
 - colliderect() - Inserir o que ele vai colidir, assim ele sabera que colidiu com o que você definiu

pygame.draw.rect() - Iremos desenhar um retangulo - "Aonde ele vai ser pintando, qual cor?, Qual padrão ele terá? " - Obs. Fazer isso toda vez que precisa pintar algo na tela
 - Possui uma função center - para centralizar 

pygame.draw.circle() - Iremos desenhar um circulo - "Aonde ele vai ser pintando, qual cor?, Qual padrão ele terá?, qual o raio? " - Obs. Fazer isso toda vez que precisa pintar algo na tela

pygame.mixer.Sound() = Colocaremos o caminho do som que precisamos, ele é uma função que mexe com som
 - .play() - Tocar o som selecionado
   - (-1) - Ele toca em looping