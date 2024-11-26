import pytest

from tasks_manager.tasks_manager_greenatom.general_code.db import DataBase


@pytest.fixture()
def task():
    d_b = DataBase()
    d_b.add_task('A', 'b', 'c', '1', '2')
    return d_b.get_all()


def test_add_task(task):
    assert task == [(1, 'A', 'b', 'c', 1, '2')]


if __name__ == '__main__':
    pytest.main()
