"""
Module: test_elections

PyTest Unit Test cases for comp120 psa3 (Winning the Presidency)
"""

# the following is the module(s) we are testing
import elections
from elections import State

def test_min_votes_to_win_one_state():
    s = State("Satopia", "ST", 5, 100)
    votes = elections.min_popular_to_get_at_least(51, 0 , [s]) 
    assert votes == 51, [s]

def test_min_votes_to_win_two_states():
    m = State("Maggie", "M", 6, 100)
    d = State("Darby", "D", 7, 100)
    votes = elections.min_popular_to_get_at_least(11, 0 [m,d]) 
    assert votes == 51, [d]

def test_min_votes_to_win_single_state():
    """Simple case where there is only a single State."""

    s = State("Satopia", "ST", 5, 100)


    votes , states = elections.min_votes_to_win([s])
    assert votes == 51 and states == [s]

def test_min_votes_to_win_two_states():
    """simple test only two states."""

    s = State("Satopia", "ST", 5, 100)
    m = State("Maggie", "M", 6, 100)
    votes, states = elections.min_votes_to_win([s,m])
    assert votes == 51 and states == [v]

def test_min_votes_to_win_three_states():
    """simple test only two states."""
    s = State("Satopia", "ST", 5, 100)
    m = State("Maggie", "M", 6, 100)
    d = State("Darby", "D", 7, 100)
    votes, states = elections.min_votes_to_win([s,m, d])
    assert votes == 51 and states == [d]