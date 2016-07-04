from time import sleep


class MyClass:
    @staticmethod
    def sum(a, b):
        return a + b


class Api:
    _users = []

    def get_formatted_users(self):
        users = self.get_users_from_db()
        formatted_users = '\n'.join(
            '{0}: {1}'.format(i + 1, user) for i, user in enumerate(users))
        return formatted_users

    def create_user(self, user):
        sleep(1)
        self._users.append(user)

    def get_users_from_db(self):
        sleep(1)
        return self._users
