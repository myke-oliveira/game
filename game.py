import random

class Character:
    def __init__(self, name: str, life: float, level: float) -> None:
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self) -> str:
        return self.__name
    
    def get_live(self) -> str:
        return self.__life
    
    def get_level(self) -> str:
        return self.__level
    
    def get_details(self) -> str:
        return f"Name: {self.__name}\nVida: {self.__life:.2f}\nNível: {self.__level}"
    
    def is_alive(self) -> bool:
        return self.__life > 0
    
    def get_damage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = random.normalvariate(self.__level * 2, 1)
        target.get_damage(damage)
        return damage


class Hero(Character):
    def __init__(self, name, live, level, skill) -> None:
        super().__init__(name, live, level)
        self.__skill = skill

    def get_skill(self) -> str:
        return self.__skill

    def get_details(self) -> str:
        return super().get_details() + f"\nHabilidade: {self.__skill}"
    
    def special_attack(self, target):
        damage = random.normalvariate(self.get_level() * 5, 1)
        target.get_damage(damage)
        return damage


class Enimy(Character):
    def __init__(self, name, life, level, nature) -> None:
        super().__init__(name, life, level)
        self.__nature = nature

    def get_nature(self) -> None:
        return self.__nature

    def get_details(self) -> str:
        return super().get_details() + f"\nNatureza: {self.__nature}"


class Game:
    """Classe orquestradora do jogo"""

    def __init__(self, hero, enimy) -> None:
        self.hero = hero
        self.enimy = enimy

    def battle(self):
        """Fazer a gestão de turnos"""
        print("Iniciando Batalha")

        while self.hero.is_alive() and self.enimy.is_alive():
            print()
            print("Detalhe dos personangens")
            print("========================")
            print("Heroi:")

            print(self.hero.get_details())
            print()
            print("Inimigo:")
            print(self.enimy.get_details())

            input("Pressione [Enter] para atacar...")

            option = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial) ")

            if option == "1":
                damage = self.hero.attack(self.enimy)
                print(f"{self.hero.get_name()} atacou {self.enimy.get_name()} e causou {damage:.2f} de dano.")
            elif option == "2":
                damage = self.hero.special_attack(self.enimy)
                print(f"{self.hero.get_name()} usou a {self.hero.get_skill()} contra {self.hero.get_name()} e causou {damage:.2f} de dano.")
            else:
                print("Opção inválida")

            damage = self.enimy.attack(self.hero)
            print(f"{self.enimy.get_name()} atacou {self.hero.get_name()} e causou {damage:.2f} de dano.")

        if self.hero.is_alive():
            print(f"Parabéns, você derrotou o {self.enimy.get_name()}")
        else:
            print(f"Você foi derrotado pelo {self.enimy.get_name()}")


def main():
    hero = Hero("Hercules", 100, 5, "Super Força")
    enimy = Enimy("Morcego", 100, 3, "Voador")
    game = Game(hero, enimy)
    game.battle()

if __name__ == "__main__":
    main()
