import doctest
from typing import List, Tuple


class PolytechnicUniversity:
    def __init__(self, name: str, students: List[str], courses: List[str]):
        """
        Инициализирует объект класса "Политехнический университет".

        :param name: Название университета.
        :param students: Список студентов университета.
        :param courses: Список предметов.

        Пример:
        # Инициализация экземпляра класса
        >>> university_name = "Polytechnic University"
        >>> student_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> course_list = ["OOP", "Reverse engineering", "Number-theoretic methods in cryptography"]
        >>> polytechnic_university = PolytechnicUniversity(university_name, student_list, course_list)
        >>> print(polytechnic_university.name)
        Polytechnic University
        >>> print(polytechnic_university.students[2])
        Okhlopkov
        >>> print(polytechnic_university.courses[0])
        OOP
        """

        if not isinstance(name, str):
            raise TypeError("University name must be a string")

        if not isinstance(students, list) or not all(isinstance(student, str) for student in students):
            raise TypeError("Students must be a list of strings")

        if not isinstance(courses, list) or not all(isinstance(course, str) for course in courses):
            raise TypeError("Courses must be a list of strings")

        self.name: str = name
        self.students: List[str] = students
        self.courses: List[str] = courses

    def conduct_exam(self, course_name: str, exam_date: str) -> List[str]:
        """
        Проводит экзамен по выбранному курсу.

        :param course_name: Название курса.
        :param exam_date: Дата экзамена.
        :return: Список студентов, сдавших экзамен.

        Пример:
        >>> university_name = "Polytechnic University"
        >>> student_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> course_list = ["OOP", "Reverse engineering", "Number-theoretic methods in cryptography"]
        >>> polytechnic_university = PolytechnicUniversity(university_name, student_list, course_list)

        # Экзамен по предмету "Теоретико-числовые методы в криптографии" в канун Нового Года
        >>> exam_results = polytechnic_university.conduct_exam(course_list[2], "31-12-2023")
        >>> print(exam_results)
        True
        """

        if not isinstance(course_name, str):
            raise TypeError("Course name must be a string")

        if not isinstance(exam_date, str):
            raise TypeError("Exam date must be a string")

        # Реализация метода...

        return True

    def expel_student(self, student_name: str) -> bool:
        """
        Отчисляет студента из университета.

        :param student_name: Имя студента, которого нужно отчислить.
        :return: Успешность отчисления студента.

        Пример:
        >>> university_name = "Polytechnic University"
        >>> student_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> course_list = ["OOP", "Reverse engineering", "Number-theoretic methods in cryptography"]
        >>> polytechnic_university = PolytechnicUniversity(university_name, student_list, course_list)

        # Отчисление студента Рудского
        >>> expulsion_result = polytechnic_university.expel_student("Rudskoy")
        >>> print(expulsion_result)
        True
        """

        if not isinstance(student_name, str):
            raise TypeError("Student name must be a string")

        # Реализация метода...

        return True

    def enroll_student(self, student_name: str, course_name: str) -> bool:
        """
        Зачисляет студента на выбранный курс.

        :param student_name: Имя студента.
        :param course_name: Название курса.
        :return: Успешность зачисления студента.

        Пример:
        >>> university_name = "Polytechnic University"
        >>> student_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> course_list = ["OOP", "Reverse engineering", "Number-theoretic methods in cryptography"]
        >>> polytechnic_university = PolytechnicUniversity(university_name, student_list, course_list)

        # Зачисление студента Зегжды на курс ООП
        >>> enrollment_result = polytechnic_university.enroll_student("Zegzhda", "OOP")
        >>> print(enrollment_result)
        True
        """

        if not isinstance(student_name, str):
            raise TypeError("Student name must be a string")

        if not isinstance(course_name, str):
            raise TypeError("Course name must be a string")

        # Реализация метода...

        return True


class PokerGame:
    def __init__(self, players: List[str], deck: List[Tuple[str, str]]):
        """
        Инициализирует объект класса "Игра в покер".

        :param players: Список игроков.
        :param deck: Колода карт, представленная в виде списка кортежей (масть, значение).

        Пример:
        # Инициализация экземпляра класса
        >>> player_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> deck_list = [('Hearts', '10'), ('Diamonds', 'J'), ('Clubs', 'Q'), ('Spades', 'K'), ('Hearts', 'A')]
        >>> poker_game = PokerGame(player_list, deck_list)
        >>> print(poker_game.players)
        ['Rudskoy', 'Zegzhda', 'Okhlopkov']
        >>> print(poker_game.deck[1])
        ('Diamonds', 'J')
        """
        if not isinstance(players, list) or not all(isinstance(player, str) for player in players):
            raise TypeError("Players must be a list of strings")

        if not isinstance(deck, list) or not all(isinstance(card, tuple) and len(card) == 2 for card in deck):
            raise TypeError("Deck must be a list of tuples (suit, value)")

        self.players: List[str] = players
        self.deck: List[Tuple[str, str]] = deck

    def deal_cards(self, num_cards: int) -> List[Tuple[str, str]]:
        """
        Раздает карты игрокам.

        :param num_cards: Количество карт, которое нужно раздать каждому игроку.
        :return: Список разданных карт.

        Пример:
        >>> player_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> deck_list = [('Hearts', '10'), ('Diamonds', 'J'), ('Clubs', 'Q'), ('Spades', 'K'), ('Hearts', 'A')]
        >>> poker_game = PokerGame(player_list, deck_list)

        # Раздача по 5 карт каждому игроку
        >>> dealt_cards = poker_game.deal_cards(5)
        """
        if not isinstance(num_cards, int) or num_cards <= 0:
            raise ValueError("Number of cards must be a positive integer")

        # Реализация метода ...

        ...


    def evaluate_hand(self, hand: List[Tuple[str, str]]) -> str:
        """
        Оценивает комбинацию карт в руке игрока.

        :param hand: Рука игрока, представленная списком карт.
        :return: Оценка комбинации карт в руке.

        Пример:
        >>> player_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> deck_list = [('Hearts', '10'), ('Diamonds', 'J'), ('Clubs', 'Q'), ('Spades', 'K'), ('Hearts', 'A')]
        >>> poker_game = PokerGame(player_list, deck_list)

        # Оценка комбинации в руке
        >>> hand_evaluation = poker_game.evaluate_hand([('Diamonds', 'A'), ('Hearts', 'A')])
        """
        if not isinstance(hand, list) or not all(isinstance(card, tuple) and len(card) == 2 for card in hand):
            raise TypeError("Hand must be a list of tuples (suit, value)")

        # Реализация метода ...

        ...


    def place_bet(self, player: str, amount: int) -> bool:
        """
        Размещает ставку от игрока.

        :param player: Имя игрока.
        :param amount: Сумма ставки.
        :return: Успешность размещения ставки.

        Пример:
        >>> player_list = ["Rudskoy", "Zegzhda", "Okhlopkov"]
        >>> deck_list = [('Hearts', '10'), ('Diamonds', 'J'), ('Clubs', 'Q'), ('Spades', 'K'), ('Hearts', 'A')]
        >>> poker_game = PokerGame(player_list, deck_list)

        # Размещение ставки от игрока "Rudskoy" в размере 50
        >>> bet_result = poker_game.place_bet("Rudskoy", 50)
        """
        if not isinstance(player, str):
            raise TypeError("Player must be a string")

        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Bet amount must be a positive integer")

        # Реализация метода ...

        ...


class SocialNetwork:
    def __init__(self, name: str, users_count: int):
        """
        Инициализирует объект класса "Социальная сеть".

        :param name: Название социальной сети.
        :param users_count: Количество пользователей в социальной сети.

        Пример:
        # Инициализация экземпляра класса
        >>> social_network = SocialNetwork("VTeleInstaK", 8_028_504_258)
        >>> print(social_network.name)
        VTeleInstaK
        >>> print(social_network.users_count)
        8028504258
        """

        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(users_count, int) or users_count < 0:
            raise ValueError("Users count must be a non-negative integer")

        self.name: str = name
        self.users_count: int = users_count

    def create_profile(self, user_id: int, username: str):
        """
        Создает профиль.

        :param user_id: Идентификационный номер пользователя.
        :param username: Имя пользователя.

        Пример:
        >>> social_network = SocialNetwork("VTeleInstaK", 8_028_504_258)

        # Создание профиля для пользователя "Zegzhda"
        >>> social_network.create_profile(1, "Zegzhda")
        """

        if not isinstance(user_id, int) or user_id < 0:
            raise ValueError("User ID must be a non-negative integer")
        if not isinstance(username, str):
            raise TypeError("Username must be a string")

        # Реализация метода ...

        ...

    def add_friend(self, user_id: int, friend_id: int):
        """
        Добавляет друга.

        :param user_id: Идентификационный номер пользователя.
        :param friend_id: Идентификационный номер друга.

        Пример:
        >>> social_network = SocialNetwork("VTeleInstaK", 8_028_504_258)

        # Пользователь id = 1 добавляет друга id = 2
        >>> social_network.add_friend(1, 2)
        """

        if not isinstance(user_id, int) or user_id < 0:
            raise ValueError("User ID must be a non-negative integer")
        if not isinstance(friend_id, int) or friend_id < 0:
            raise ValueError("Friend ID must be a non-negative integer")

        # Реализация метода ...

        ...

    def post_status(self, user_id: int, status_text: str):
        """
        Публикация статуса.

        :param user_id: Идентификационный номер пользователя.
        :param status_text: Текст статуса.

        Пример:
        >>> social_network = SocialNetwork("VTeleInstaK", 8_028_504_258)

        # Пользователь id = 1 публикует статус "Сессия уже скоро, бедные студентики :)"
        >>> social_network.post_status(1, "Сессия уже скоро, бедные студентики :)")
        """

        if not isinstance(user_id, int) or user_id < 0:
            raise ValueError("User ID must be a non-negative integer")
        if not isinstance(status_text, str):
            raise TypeError("Status text must be a string")

        # Реализация метода ...

        ...

if __name__ == "__main__":
    doctest.testmod()
