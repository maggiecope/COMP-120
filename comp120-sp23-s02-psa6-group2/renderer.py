"""
This file contains the Blocky Renderer class.

DO NOT MODIFY THIS FILE!
"""
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PACIFIC_POINT = (1, 128, 181)
OLD_OLIVE = (138, 151, 71)
REAL_RED = (199, 44, 58)
MELON_MAMBO = (234, 62, 112)
DAFFODIL_DELIGHT = (255, 211, 92)
TEMPTING_TURQUOISE = (75, 196, 213)
COLOR_LIST = [PACIFIC_POINT, REAL_RED, OLD_OLIVE, DAFFODIL_DELIGHT]
COLOR_NAMES = ['Pacific Point', 'Real Red', 'Old Olive', 'Daffodil Delight']

BOARD_WIDTH = 750
BOARD_HEIGHT = 750
TEXT_HEIGHT = 75


def color_name(color: tuple[int, int, int]) -> str:
    """Return the color name associated with this color value, or
    the empty string if this color value isn't in our color list.
    """
    for i in range(len(COLOR_LIST)):
        if COLOR_LIST[i] == color:
            return COLOR_NAMES[i]
    return ''


class Renderer:
    """
    A class designed to handle the drawing and context for the board

    === Attributes ===
    displayed_image:
         image to draw to the screen for visualization
    screen:
         the pygame context to show
    window_size:
         The height and width of the rendering window, in pixels.
    player_labels:
         list of player icons to display
    """
    displayed_image: pygame.Surface
    screen: pygame.Surface
    window_size: tuple[int, int]
    player_labels: list[pygame.Surface]

    def __init__(self, num_players: int) -> None:
        """Initialize this renderer.

        <num_players> is the total number of players in this Game.  It is
        used to render a label showing the player whose move it is at any
        given time.
        """
        pygame.init()
        self.displayed_image = \
            pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT + 75))
        self.screen = \
            self.displayed_image.subsurface(((0, 0),
                                             (BOARD_WIDTH, BOARD_HEIGHT)))
        self.screen.fill(WHITE)

        font = pygame.font.SysFont(None, 25)
        self.player_labels = [
            font.render(f'PLAYER {i}', True, MELON_MAMBO, (0, 0, 0))
            for i in range(num_players)
        ]

        self.displayed_image.blit(self.player_labels[0], (0, BOARD_HEIGHT))
        self._render_text_help()

    def _render_text_help(self):
        """Add the UI text onto the display."""
        font = pygame.font.SysFont(None, 25)
        self.displayed_image.blit(
            font.render("LMB: rotate CW           " +
                        "RMB: rotate CCW         ",
                        True,
                        (255, 255, 255)), (0, BOARD_HEIGHT + 25)
        )
        self.displayed_image.blit(
            font.render("H: Swap Horizontally     " +
                        "V: Swap Vertically     " +
                        "S: Smash Cell     " +
                        "Up/Down: Change selection",
                        True,
                        (255, 255, 255)), (0, BOARD_HEIGHT + 50)
        )

    def draw(self, board: 'Block', player_id: int) -> None:
        """Clear the canvas and draw the blocks."""
        # draw the background map onto the screen
        self.screen.fill(WHITE)

        selected = []
        for color, pos, size, width in board.rectangles_to_draw():
            if color == TEMPTING_TURQUOISE:
                selected.append((color, pos, size, width))
            else:
                pygame.draw.rect(self.screen, color, (pos, size), width)

        # Draw highlighted rectangle borders last
        for color, x, y, width in selected:
            pygame.draw.rect(self.screen, color, (x, y), width)

        self.displayed_image.blit(
            self.player_labels[player_id], (0, BOARD_HEIGHT))
        pygame.display.update()

        # Check for new events; this should avoid the OSX issue for delayed
        # updating of the pygame window.
        pygame.event.peek([])

    # For game start
    def display_goal(self, player: 'Player') -> None:
        """Display the goal for the given player.
        """
        self._message_box(WHITE, f'Click to see player {player.id}\'s goal')
        self._message_box(player.goal.color,
                          f'Goal is: {player.goal.description()}')

    def _message_box(self, color: tuple[int, int, int], message: str) -> None:
        """Render a message in Pygame and and wait for a click.

        Modified from
        http://archives.seul.org/pygame/users/May-2005/msg00008.html.
        """
        screen = self.screen
        screen.fill(color)
        font = pygame.font.Font(None, 18)
        rect = pygame.Rect([0, 0, 400, 22])
        rect.center = screen.get_rect().center

        pygame.draw.rect(screen, WHITE, rect, 1)
        pygame.draw.rect(screen, BLACK, rect, 0)

        offset = (3, 3)
        rect.left += offset[0]
        rect.top += offset[1]

        if len(message) > 0:
            screen.blit(font.render(message, 1, WHITE), rect.topleft)

        pygame.display.flip()

        # Wait for user click
        while True:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    return
