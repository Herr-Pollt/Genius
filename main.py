from screen import Screen
from game import Game

def main():
    screen = Screen()
    game = Game()
    while True:
        action = screen.MakeScreen()
        if action == "next_screen":
            game.start()

if __name__ == "__main__":
    main()