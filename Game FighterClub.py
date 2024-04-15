import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        # Уменьшаем здоровье противника на величину силы атаки
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        # Проверяем, жив ли герой
        return self.health > 0

class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Битва героев началась!")
        # Определяем, кто будет атаковать первым (случайным образом)
        turn = random.choice([self.player, self.computer])

        # Игра продолжается, пока оба героя живы
        while self.player.is_alive() and self.computer.is_alive():
            if turn == self.player:
                self.player.attack(self.computer)
                turn = self.computer
            else:
                self.computer.attack(self.player)
                turn = self.player

            # Печатаем текущее состояние здоровья героев
            print(
                f"Здоровье {self.player.name}: {self.player.health}, Здоровье {self.computer.name}: {self.computer.health}")

            # Ждем следующего хода
            input("Нажмите Enter для продолжения...")

        # Объявляем победителя
        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print("Компьютер победил!")


# Запуск игры
player_name = input("Введите имя игрока: ")
game = Game(player_name)
game.start()