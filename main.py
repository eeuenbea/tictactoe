import pygame

pygame.init()

screen = pygame.display.set_mode((900, 643))

board_img = pygame.image.load("tictacsus.png")

font = pygame.font.SysFont(None, 200)

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

turn = 0

done = False
while True:
    screen.blit(board_img, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and (turn == 9 or done):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        turn = 0
        done = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and not done:
            y = 0
            x = 0
            if pygame.mouse.get_pos()[0] < 365:
                x = 0
            if 541 > pygame.mouse.get_pos()[0] >= 365:
                x = 1
            if 713 > pygame.mouse.get_pos()[0] >= 541:
                x = 2
            if pygame.mouse.get_pos()[1] < 220:
                y = 0
            if 220 <= pygame.mouse.get_pos()[1] < 415:
                y = 1
            if pygame.mouse.get_pos()[1] >= 415:
                y = 2
            if board[y][x] == " ":
                if turn % 2 == 0:
                    board[y][x] = "x"
                else:
                    board[y][x] = "o"
                turn += 1

    P = font.render("O", True, (0, 0, 0))
    X = font.render("X", True, (0, 0, 0))
    x = 0
    y = 0
    for row in board:
        for letter in row:
            # print(board)
            if letter == "x":
                screen.blit(X, (x * 180 + 225, y * 180 + 75))
            if letter == "o":
                screen.blit(P, (x * 180 + 225, y * 180 + 75))
            x += 1
        x = 0
        y += 1

    if board[0][0] == board[0][1] == board[0][2] != " ":
        print("win")
        done = True
    if board[1][0] == board[1][1] == board[1][2] != " ":
        print("win")
        done = True
    if board[2][0] == board[2][1] == board[2][2] != " ":
        print("win")
        done = True
    if board[0][0] == board[1][0] == board[2][0] != " ":
        print("win")
        done = True
    if board[0][1] == board[1][1] == board[2][1] != " ":
        print("win")
        done = True
    if board[0][2] == board[1][2] == board[2][2] != " ":
        print("win")
        done = True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print("win")
        done = True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print("win")
        done = True
    pygame.display.flip()
input()
