"""testing space for the functions made in utils"""

__author__ = "730762790"

from exercises.ex05.utils import only_evens

def test_only_evens_usecase () -> None: ## these unit test, test that this function behaves correctly by returning the evens 
    """returns only evens from the list"""
    d: list [int] = [3,5,4,6] 
    assert only_evens (d) == [4,6]
def test_only_evens_edgecase ()-> None: 
    """test cases with an empty list"""
    assert only_evens ([]) == []
def test_only_evens_no_evens_usecase () -> None: 
    """testing when only odd numbers"""
    assert only_evens ([3,5,7,9]) == []



from exercises.ex05.utils import sub

def test_sub_usecase () -> None: ## these unit test, test that this function is able to spit out the right element in that index 
    """test to make sure the inputed start and end index is given"""
    assert sub ([4,5,6,7], 1, 3) == [5,6]
def test_sub_negative_start():
    """test with a negative start index."""
    assert sub([10, 20, 30], -1, 2) == [10, 20]
def test_sub_out_of_bounds():
    """test with out of bounds indices."""
    assert sub([], 1, 3) == []


from exercises.ex05.utils import add_at_index

def test_add_usecase () -> None:  ## these unit test, test that this function is able to add
    """testing mutation of addition of elements"""
    list_1 = [13, 14, 15, 16]
    add_at_index (list_1, 11, 0)
    assert list_1 == [11, 13, 14, 15, 16]
def test_addempty_edgecase () -> None: 
    """adding elements into a list"""
    list_2 = []
    add_at_index (list_2, 5, 0)
    assert list_2 == [5] 

import pytest 
def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    list_3 = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(list_3, 4, 4)  
