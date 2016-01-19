import pytest

from lumido import Cronjob

@pytest.mark.parametrize('mins, hours, result', [(30, 1, (130, 'tomorrow')), (45, '*', (1645, 'today')),
                                                 ('*', '*', (1610, 'today')), ('*', 19, (1900, 'today'))])
def test_next(mins, hours, result):
    cron = Cronjob(mins, hours)

    assert cron._next(1610) == result
