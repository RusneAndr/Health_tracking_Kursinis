#user_factory.py
#User Factory

from Person import New_user, Already_user

class UserFactory:
    @staticmethod
    def get_user(user_type, *args, **kwargs):
        if user_type == "new":
            return New_user(*args, **kwargs)
        elif user_type == "existing":
            return Already_user(*args, **kwargs)
        raise ValueError("Invalid user type provided")
