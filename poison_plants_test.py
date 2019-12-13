import pytest

from poison_plants_hackerrank import Plants


@pytest.fixture
def plant():
    p = Plants()

    return p

def test_days(plant):

    assert(plant.poisonousPlants([]) == 0)
    assert(plant.poisonousPlants([9]) == 0)
    assert(plant.poisonousPlants([9, 1]) == 0)
    assert(plant.poisonousPlants([1, 9]) == 1)
    assert(plant.poisonousPlants([1, 2, 5, 6, 9]) == 1)
    assert(plant.poisonousPlants([6, 5, 8, 4, 7, 10, 9]) == 2)
    assert(plant.poisonousPlants([3, 2, 5, 4]) == 2)
    assert(plant.poisonousPlants([4, 3, 7, 5, 6, 4, 2]) == 3)