# Task 2
# Implement tests in pytest approaches for some previously solved tasks and then compare results and code amount
# with Task 1.

import pytest
from tvcontroller import TVController


def test_current_channel(tv):
    assert tv.current_channel() == "BBC"


def test_first_channel(tv):
    assert tv.first_channel() == "BBC"


def test_last_channel(tv):
    assert tv.last_channel() == "TV1000"


def test_turn_channel(tv):
    assert tv.turn_channel(2) == "Discovery"


def test_turn_channel_not_exist(tv):
    # try:
    # tv.turn_channel(10)
    # except ValueError as e:
    # assert str(e) == "Channel 10 is not in ['BBC', 'Discovery', 'TV1000']"

    with pytest.raises(ValueError) as ctx:
        tv.turn_channel(10)
    assert str(ctx.value) == "Channel 10 is not in ['BBC', 'Discovery', 'TV1000']"


def test_next_channel(tv):
    assert tv.next_channel() == "Discovery"


@pytest.fixture
def tv():
    controller = TVController(["BBC", "Discovery", "TV1000"])
    yield controller

    controller.first_channel()
