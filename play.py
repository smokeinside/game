import moves
from games import Game
from players import Player

if __name__ == "__main__":
    defalut_moves = [
        moves.Attack(18, 25, name="Simple attack"),
        moves.Attack(10, 35, name="Wide range attack"),
        moves.Heal(18, 25, name="Simple self heal", is_self_action=True),
    ]
    computer = Player("Computer", defalut_moves, moves.IncreasedHealMoveSelector(35))
    player = Player("Alexander", defalut_moves, moves.MoveSelector())
    game = Game([computer, player])
    game.play()
