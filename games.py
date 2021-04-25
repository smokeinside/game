import logging
import random
from typing import List

from players import Player

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name=__name__)


class Game:
    def __init__(self, players: List[Player]):
        self.players = players

    def play(self) -> Player:
        executor, target = random.sample(self.players, 2)
        while True:
            executor.make_move(target)
            if target.health == 0:
                logger.info(
                    f"{executor} has won in the battle with {target} and has {executor.health} health left"
                )
                return executor
            else:
                logger.info(
                    f"Round result: {executor} has {executor.health} health; {target} has {target.health} health"
                )
            executor, target = target, executor
