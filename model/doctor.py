from model.user import User


class Doctor(User):

    def show_menu(self, db):
        print("1 - show schedule")
