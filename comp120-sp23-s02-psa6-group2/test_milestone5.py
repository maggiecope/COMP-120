"""
Test cases for Milestone 5.
"""
from helpers import equal_boards, construct_board

from block import Block

def test_swap():
    """Test the swapping of blocks in the tree.

    - Test against all of the standard boards, at different levels
    - Ensure the board changes when one swap is performed
    - Ensure that doing the same swap twice results in the original board
    """
    # A board to mutate.
    board, _ = construct_board()
    # A board to store the expected result.
    ans_board, _ = construct_board()
    # Another copy of the original board to compare against once we have
    # mutated board.
    ref_board, _ = construct_board()

    # Swap one direction and check resulting board
    board.swap(0)
    # By hand, make ans_board hold the correct answer.
    ans_board.children = [
        ans_board.children[1],
        ans_board.children[0],
        ans_board.children[3],
        ans_board.children[2]
    ]
    assert equal_boards(board, ans_board),\
        'Swapping does not match the reference configuration'

    # Swap the same direction again and ensure the operation is undone
    board.swap(0)
    assert equal_boards(board, ref_board),\
        'Performing same swap twice does not undo the operation'


def test_rotate():
    """Test the rotating of blocks in the tree

    - Test against all of the standard boards
    - Ensure the board changes when one rotation is performed
    - Ensure that doing opposite rotations results in the original board
    """
    board, _ = construct_board()
    # The board to modify
    ans_board, _ = construct_board()
    # What the tree should look like
    ref_board, _ = construct_board()

    # Rotate one of the children manually
    ans_board.children[0].children = [
        ans_board.children[0].children[1],
        ans_board.children[0].children[2],
        ans_board.children[0].children[3],
        ans_board.children[0].children[0]
    ]

    # Rotate one direction and check resulting board
    board.children[0].rotate(1)
    assert equal_boards(board, ans_board)
    # Rotate the opposite direction and ensure the operation is undone
    board.children[0].rotate(3)
    assert equal_boards(board, ref_board)


def test_smash():
    """Test to see if the block's children change after the smash operation.

    - Confirm that smashing has no effect where it is not allowed (at root
      node or at the max_depth)
    - This operation is random, so cannot
      check for an exact result, only whether the block state has changed
    """
    board, _ = construct_board()

    # What the tree should look like
    ref_board, _ = construct_board()

    # Cannot smash on the root block
    board.smash()
    assert equal_boards(board, ref_board)

    # Cannot smash on leaf block
    board.children[0].children[0].smash()
    assert equal_boards(board, ref_board)

    # Smash another block
    board.children[0].smash()
    assert not equal_boards(board, ref_board),\
        'A legal smash changed nothing; unlikely, but not necessarily an error'


if __name__ == "__main__":
    import pytest
    pytest.main(['test_milestone5.py'])

