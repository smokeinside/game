import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name=__name__)


class ValidationError(Exception):
    pass


class Player:
    def __init__(self, name, moves, move_selector, health=100, max_health=100):
        self.name = name
        self.moves = moves
        self.move_selector = move_selector
        self.max_health = max_health
        self.health = health

    @property
    def moves(self):
        return self._moves

    @moves.setter
    def moves(self, value):
        if not isinstance(value, list) or len(value) < 1:
            raise ValidationError(
                "Moves has to be list of length greater or equal to 1"
            )
        self._moves = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value > self.max_health:
            raise ValidationError(
                f"Health value is {value} which is greater then {self.max_health}"
            )
        if value < 0:
            raise ValidationError(
                f"Health value is {value.health} which is lower then 0"
            )
        if hasattr(self, "_health"):
            logger.info(f"{self} health changed from {self._health} to {value}")
            self._health = value
        else:
            self._health = value
            logger.info(f"{self} health was initialized as {self._health}")

    def make_move(self, opponent):
        move = self.move_selector.select(self, self.moves)
        target = self if move.is_self_action else opponent
        move.execute(target)

    def __str__(self):
        return self.name
