#Strategy Pattern

from abc import ABC, abstractmethod

class AttackStrategy(ABC):
    @abstractmethod
    def attack(self) -> None:
        pass

class AirAttack(AttackStrategy):
    def attack(self) -> None:
        print("Atacando desde el Aire")

class GroundAttack(AttackStrategy):
    def attack(self) -> None:
        print("Atacando desde la Tierra")

class NavalAttack(AttackStrategy):
    def attack(self) -> None:
        print("Atacando desde el Agua")


class MilitaryUnit:
    def __init__(self, attack_strategy: AttackStrategy) -> None:
        self.attack_strategy = attack_strategy

    def perform_attack(self):
        self.attack_strategy.attack()


if __name__ == '__main__':
    air_attack = AirAttack()
    ground_attack = GroundAttack()

    unit = MilitaryUnit(air_attack)
    unit.perform_attack()

    unit2 = MilitaryUnit(ground_attack)
    unit2.perform_attack()