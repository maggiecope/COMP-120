
"""
Test cases for Milestone 4.
"""
from helpers import equal_boards, construct_board


def test_get_selected_block():
    """Test the selection process for getting individual blocks out of the board

    - Given a location and level, return correct part of the tree
    - Ensure that if the selection level is too deep or too shallow,
      a block is still returned
    """
    board, _ = construct_board()
    board.update_block_locations((0, 0), 50)

    assert equal_boards(board.children[0].children[0],
                        board.get_selected_block((40, 10), 2))
    assert equal_boards(board.children[0],
                        board.get_selected_block((40, 10), 1))
    assert equal_boards(board,
                        board.get_selected_block((40, 10), 0))

    # Always needs to return a block
    assert board.get_selected_block((100, 100), 0) is not None
    assert board.get_selected_block((-10, -10), 0) is not None
    assert board.get_selected_block((10, 100), 0) is not None
    assert board.get_selected_block((100, 10), 0) is not None


if __name__ == "__main__":
    import pytest
    pytest.main(['test_milestone4.py'])

