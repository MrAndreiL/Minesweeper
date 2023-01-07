import pygame
import os
import random


class Game:
    """Minesweeper main board game.

    This class takes care of initiating, creating
    and updating the main pygame interface. It imports
    assets and deals with input from user.
    """

    def __init__(self, board):
        """Constructor method that builds up pygame instance.

        Establishes the main parameters that will be used
        throughout the whole game, initiates the pygame instance
        and sets up the window.

        Args:
            board: Info_Board type object that describes how to build
                the actual game board.
        """
        # Main board build-up information.
        self._BLOCK_WIDTH = 20
        self._BLOCK_HEIGHT = 20

        self.buffer = int((20 * self._BLOCK_WIDTH * board.rows) / 100)

        self._BOARD_WIDTH = self._BLOCK_WIDTH * board.columns
        self._BOARD_HEIGHT = (self._BLOCK_HEIGHT * board.rows) + self.buffer

        # Commonly used color codes.
        self._WHITE = (255, 255, 255)

        # Input data.
        self._ROWS = board.rows
        self._COLUMNS = board.columns
        self._BOMBS = board.bombs
        self._SECONDS = board.seconds

        # Pygame init data and maintainance.
        pygame.init()

        pygame.display.set_caption("Minesweeper")

        self._BOARD = pygame.display.set_mode(
                (self._BOARD_WIDTH,
                 self._BOARD_HEIGHT)
        )

        self._FRAMES = 30

        self._CLOCK = pygame.time.Clock()

    def update_struct(self, pos, board):
        """Updates the board structure according to the player's action.

        Changes the state of a block in the given structure if
        that certain block was actioned by the player.

        Args:
            board: Dictionary mapping the game board.
            pos: Click coordinates.

        Returns:
            An updated version of the board dictionary. It
            showcases the changes made by the players' action.
        """
        if pos[1] < self.buffer:
            return board
        # Iterate through the list and find the corresponding rect.
        for item in board.items():
            if item[1][0].collidepoint(pos):
                board[item[0]][2] = 1
                break
        return board

    def is_neighbour(self, xi, xj):
        """Asserts if two positions are adjacent.

        Args:
            Xi: first position tuple
            Xj: second position tuple

        Returns:
            A boolean value. True if the positions
                are adjacent. False otherwise.
        """
        # line/row adjacent.
        if xi[0] - 1 == xj[0] and xi[1] == xj[1]:
            return True

        if xi[0] + 1 == xj[0] and xi[1] == xj[1]:
            return True

        # column adjcent.
        if xi[1] - 1 == xj[1] and xi[0] == xj[0]:
            return True

        if xi[1] + 1 == xj[1] and xi[0] == xj[0]:
            return True

        # cross adjacent.
        if xi[0] - 1 == xj[0] and xi[1] - 1 == xj[1]:
            return True

        if xi[0] - 1 == xj[0] and xi[1] + 1 == xj[1]:
            return True

        if xi[0] + 1 == xj[0] and xi[1] + 1 == xj[1]:
            return True

        if xi[0] + 1 == xj[0] and xi[1] - 1 == xj[1]:
            return True

        return False

    def bomb_distance(self, pos, bombs):
        """Finds out how many bombs are adjacent with a position.

        Looks up in vecinity of a given position and determines the
        number of adjacent bombs.

        Args:
            pos: tuple (i, j)
            bombs: list of positions of bombs.

        Returns:
            An integer in [0, 8] which represents the number
                of adjacent bombs.
        """
        adjacent = 0
        for bomb in bombs:
            if self.is_neighbour(pos, bomb):
                adjacent += 1
        return adjacent

    def create_game_structure(self):
        """Create a dictionary associated with the game board.

        Builds a dictionary that associates the (i, j in {1, n})
        tuple position to a list consisting of a rect with the x, y
        positions properly placed, a value in [-1, 8] and 0 -> undiscovered,
        1 -> discoverd, 2 -> flag, 3 -> question mark, 4 -> bomb.
        -1 -> a bomb.
        [0, 8] -> the number of adjacent bombs.

        Returns:
            A dictionary with tuple -> tuple association.
        """
        board_structure = dict()

        rows = list(range(0, self._COLUMNS))
        cols = list(range(0, self._ROWS))
        positions = [(x, y) for x in rows for y in cols]

        # Randomly sample out bomb positions.
        bomb_positions = random.sample(positions, self._BOMBS)

        not_bombs = [(x, y) for (x, y) in positions
                     if (x, y) not in bomb_positions]

        # Place bomb positions in the dictionary.
        for bomb_pos in bomb_positions:
            rect = pygame.Rect(
                    bomb_pos[0] * self._BLOCK_WIDTH,
                    bomb_pos[1] * self._BLOCK_HEIGHT + self.buffer,
                    self._BLOCK_WIDTH,
                    self._BLOCK_HEIGHT
            )
            board_structure[bomb_pos] = [rect, -1, 0]

        # Place remaining positions in the dictionary.
        for pos in not_bombs:
            rect = pygame.Rect(
                    pos[0] * self._BLOCK_WIDTH,
                    pos[1] * self._BLOCK_HEIGHT + self.buffer,
                    self._BLOCK_WIDTH,
                    self._BLOCK_HEIGHT,
            )
            board_structure[pos] = [rect,
                                    self.bomb_distance(pos, bomb_positions),
                                    0]
        for el in board_structure.items():
            print(el[1][0])
        return board_structure

    def game_loop(self):
        """Interacts with the player and controls displaying.

        Through an infinite loop, provides the player with the
        minesweeper table and responds appropriately to their
        actions. Stops when the player exits the game.
        """

        # Import assets.
        scores = []
        spots = []
        try:
            base_path = os.path.dirname(__file__)

            # Import empty hidden block.
            empty_block = pygame.image.load(
                    os.path.join(base_path, "assets/empty-block.png")
            ).convert()
            empty_block = pygame.transform.scale(empty_block,
                                                 (self._BLOCK_WIDTH,
                                                  self._BLOCK_HEIGHT)
                                                 )

            # Import score counters and spot places.
            for i in range(0, 10):
                score = pygame.image.load(
                        os.path.join(base_path, f"assets/score_{i}.png"))
                score = pygame.transform.scale(score,
                                               (self._BLOCK_WIDTH,
                                                self._BLOCK_HEIGHT)
                                               )
                scores.append(score)

            for i in range(0, 9):
                spot = pygame.image.load(
                        os.path.join(base_path, f"assets/{i}.png"))
                spot = pygame.transform.scale(spot,
                                              (self._BLOCK_WIDTH,
                                               self._BLOCK_HEIGHT)
                                              )
                spots.append(spot)

            # Smiley faces.
            smiley = pygame.image.load(
                    os.path.join(base_path, "assets/smiley.png")
            ).convert()
            smiley = pygame.transform.scale(smiley,
                                            (self._BLOCK_WIDTH,
                                             self._BLOCK_HEIGHT)
                                            )

            smiley_cool = pygame.image.load(
                    os.path.join(base_path, "assets/smiley_cool.png")
            ).convert()
            smiley_cool = pygame.transform.scale(smiley_cool,
                                                 (self._BLOCK_WIDTH,
                                                  self._BLOCK_HEIGHT)
                                                 )

            smiley_rip = pygame.image.load(
                    os.path.join(base_path, "assets/smiley_rip.png")
            ).convert()
            smiley_rip = pygame.transform.scale(smiley_rip,
                                                (self._BLOCK_WIDTH,
                                                 self._BLOCK_HEIGHT)
                                                )

            # Bombs.
            clicked_bomb = pygame.image.load(
                    os.path.join(base_path, "assets/bomb-at-clicked-block.png")
            ).convert()
            clicked_bomb = pygame.transform.scale(clicked_bomb,
                                                  (self._BLOCK_WIDTH,
                                                   self._BLOCK_HEIGHT)
                                                  )

            unclicked_bomb = pygame.image.load(
                    os.path.join(base_path, "assets/unclicked-bomb.png")
            ).convert()
            unclicked_bomb = pygame.transform.scale(unclicked_bomb,
                                                    (self._BLOCK_WIDTH,
                                                     self._BLOCK_HEIGHT)
                                                    )

            # Flags.
            flag = pygame.image.load(
                    os.path.join(base_path, "assets/flag.png")
            ).convert()
            flag = pygame.transform.scale(flag,
                                          (self._BLOCK_WIDTH,
                                           self._BLOCK_HEIGHT)
                                          )

            flag_wrong = pygame.image.load(
                    os.path.join(base_path, "assets/wrong-flag.png")
            ).convert()
            flag_wrong = pygame.transform.scale(flag_wrong,
                                                (self._BLOCK_WIDTH,
                                                 self._BLOCK_HEIGHT)
                                                )

            question = pygame.image.load(
                    os.path.join(base_path, "assets/question.png")
            ).convert()
            question = pygame.transform.scale(question,
                                              (self._BLOCK_WIDTH,
                                               self._BLOCK_HEIGHT)
                                              )

            icon = pygame.image.load(
                    os.path.join(base_path, "assets/icon.png")
            ).convert()
        except Exception as exp:
            print("Exception raised when importing assets", exp)

        # Display game icon.
        pygame.display.set_icon(icon)

        # Receive game table structure.
        board_structure = self.create_game_structure()
        print(len(board_structure))

        # Game states => 0 - playing, 1 - reveal, 2 - win, 3 - dead
        game_state = 0

        # Infinite game loop.
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    board_structure = self.update_struct(event.pos,
                                                         board_structure)

            # Fill the screen with white.
            self._BOARD.fill(self._WHITE)

            # Redraw pieces on table.
            for piece in board_structure.items():
                if piece[1][2] == 0:  # if it was not discovered.
                    self._BOARD.blit(
                            empty_block,
                            piece[1][0]
                    )
                else:  # if discovered, replace with numbered piece or bomb.
                    if piece[1][1] > -1:
                        self._BOARD.blit(
                                spots[piece[1][1]],
                                piece[1][0]
                        )
                    else:
                        self._BOARD.blit(
                                clicked_bomb,
                                piece[1][0]
                        )
            # Update the display.
            pygame.display.flip()

            # Ensure CPU clock-frame.
            self._CLOCK.tick(self._FRAMES)

        # End-game clean-up.
        pygame.quit()
