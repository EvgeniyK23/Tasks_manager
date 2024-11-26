import sqlite3


class DataBase:

    def __init__(self, db="tasks_manager.db"):
        db = db
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Tasks "
            "(i_d INTEGER PRIMARY KEY  AUTOINCREMENT, "
            "fullname TEXT, "
            "name TEXT, "
            "descript TEXT, "
            "priority INTEGER,"
            "deadline TEXT)"
        )
        self.conn.commit()
        print("DataBase created\nСоединение восстановлено")

    def get_all(self):
        """Функция выводит всех задачи.
        Returns: Возвращает список всех задач.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks")
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")

    def add_task(
        self, fullname: str, name: str, descript: str,
            priority: int, deadline: int
    ):
        if all(
            [name.isalpha(), descript.isalpha(),
             priority.isdigit(), deadline.isalpha()]
        ):
            raise ValueError("Некорректные данные")
        try:
            self.cur.execute(
                "INSERT INTO Tasks (fullname, name, "
                "descript, priority, deadline) VALUES (?, ?, ?, ?, ?)",
                (fullname, name, descript, priority, deadline),
            )
            self.conn.commit()
        except Exception as ex:
            print(f"Ошибка {ex}")

    def delete(self, i_d: int):
        """Удаляет задачу по ID.

        Args:
            i_d: I_D задачи.
        """
        try:
            self.cur.execute("DELETE FROM Tasks WHERE i_d=?",
                             (i_d,))
            self.conn.commit()
        except Exception as ex:
            print(f"Ошибка {ex}")

    def delete_all(self):
        """Удаляет всю БД.
        """
        try:
            self.cur.execute("DROP TABLE IF EXISTS Tasks")
            self.conn.commit()
            self.conn.close()
            print("Соединение разорвал")
        except Exception as ex:
            print(f"Ошибка {ex}")

    def search_name(self, name=""):
        """Поиск задачи по названию задачи.

        Args:
            name: Название задачи.

        Returns: Возвращает список из кортежей с совпавшими названиями задач.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks WHERE name=?",
                             (name,))
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")

    def search_fullname(self, fullname=""):
        """Поиск задачи по ФИО записавшему задачу.

        Args:
            fullname: ФИО зарегистрировавшего задачу.

        Returns: Возвращает список из кортежей с совпавшими ФИО.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks WHERE fullname=?",
                             (fullname,))
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")

    def search_deadline(self, deadline=""):
        """Поиск задачи по сроку сдачи задачи.

        Args:
            deadline: Срок сдачи

        Returns: Возвращает список из кортежей с совпавшими дедлайнами задач.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks WHERE deadline=?",
                             (deadline,))
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")

    def sort_name(self):
        """Сортировка по названию задачи.

        Returns: Возвращает список кортежей с сортировкой по названию задачи.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks ORDER BY name")
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")

    def sort_fullname(self):
        """Сортировка по ФИО записавшему задачу.

        Returns: Возвращает список кортежей с сортировкой по ФИО.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks ORDER BY fullname DESC")
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")

    def sort_deadline(self):
        """Сортировка по сроку сдачи задачи.

        Returns: Возвращает список кортежей с сортировкой по дедлайну.
        """
        try:
            self.cur.execute("SELECT * FROM Tasks ORDER BY deadline")
            rows = self.cur.fetchall()
            return rows
        except Exception as ex:
            print(f"Ошибка {ex}")


if __name__ == "__main__":
    d_b = DataBase()

    print(*d_b.get_all(), sep="\n")
    print()
    print(*d_b.sort_fullname(), sep="\n")

    print()
    print(*d_b.search_fullname("A"), sep="\n")
