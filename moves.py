import logging
import random

from players import Player

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name=__name__)


class Move:
    def __init__(self, name, is_self_action=False):
        self.name = name
        self.is_self_action = is_self_action

    def execute(self, target: Player):
        raise NotImplementedError

    def __str__(self):
        return self.name


class MoveWithRange(Move):
    def __init__(self, minimum, maximum, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.minimum = minimum
        self.maximum = maximum


class Attack(MoveWithRange):
    def execute(self, target: Player):
        damage = random.randrange(self.minimum, self.maximum + 1)
        logger.info(f"{target} received {damage} damage")
        target.health = 0 if damage >= target.health else target.health - damage


class Heal(MoveWithRange):
    def execute(self, target: Player):
        heal = random.randrange(self.minimum, self.maximum + 1)
        logger.info(f"{target} received {heal} heal")
        after_heal = target.health + heal
        target.health = (
            target.max_health if after_heal > target.max_health else after_heal
        )


class MoveSelector:
    def select(self, player, moves):
        move = random.choice(moves)
        logger.info(f"{move} was chosen for {player}")
        return move


class IncreasedHealMoveSelector(MoveSelector):
    def __init__(self, critical_health):
        self.critical_health = critical_health

    def select(self, player, moves):
        if player.health <= self.critical_health:
            weights = [2.0 if isinstance(move, Heal) else 1.0 for move in moves]
        else:
            weights = [1.0 for _ in moves]
        [move] = random.choices(moves, weights)
        logger.info(f"{move} was chosen for {player}")
        return move
