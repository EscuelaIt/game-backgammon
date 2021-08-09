from src.controllers.move_piece_controller import MovePieceController
from src.models.command import Command
from src.types import GameState


class MovePieceCommand(Command):
    title = 'move {} spaces'

    def __init__(self, move_piece_controller: MovePieceController, move: int) -> None:
        self.move_piece_controller = move_piece_controller
        self.game = self.move_piece_controller.game
        self.move = move
        self.title = self.title.format(move)

    def __call__(self) -> None:
        self.move_piece_controller.move(self.move)

    def is_active(self) -> bool:
        return self.game.state == GameState.MOVING_PIECE
