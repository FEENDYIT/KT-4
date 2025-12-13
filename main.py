class User:
    count = 0

    def __init__(self, name, login, password, grade):  # Исправлено: должно быть __init__
        self._name = self._clean_name(name)
        self._login = login
        self._password = password
        self._grade = grade
        User.count += 1

    @staticmethod
    def _clean_name(name):
        return name.replace(' ', '')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = self._clean_name(value)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return '*' * len(self._password)

    @password.setter
    def password(self, value):
        self._password = value

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}")  # Исправлено: добавлен пробел

    def __lt__(self, other):  # Исправлено: должно быть __lt__
        if isinstance(other, User):
            return self._grade < other._grade
        return NotImplemented

    def __gt__(self, other):  # Исправлено: должно быть __gt__
        if isinstance(other, User):
            return self._grade > other._grade
        return NotImplemented

    def __eq__(self, other):  # Исправлено: должно быть __eq__
        if isinstance(other, User):
            return self._grade == other._grade
        return NotImplemented

    def __getattr__(self, item):  # Исправлено: должно быть __getattr__
        if item == 'grade':
            print("Неизвестное свойство grade")
            return None
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{item}'")  # Исправлено: __name__


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):  # Исправлено: должно быть __init__
        super().__init__(name, login, password, grade)  # Исправлено: super() без аргументов
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.role}")  # Добавлена роль

    def __getattr__(self, item):  # Исправлено: должно быть __getattr__
        if item == 'grade':
            print("Неизвестное свойство grade")
            return None
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{item}'")  # Исправлено: __name__


# Тестирование
user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

print(f'Всего обычных пользователей: {User.count}')
print(f'Всего супер-пользователей: {SuperUser.count}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'  # Вызовет сообщение "Невозможно изменить логин!"
print(user1.grade)   # Вызовет __getattr__ с сообщением "Неизвестное свойство grade"

# Попытка установить grade (это вызовет ошибку, так как нет сеттера)
try:
    admin.grade = 10  # Это вызовет AttributeError
except AttributeError as e:
    print(f"Ошибка: {e}")