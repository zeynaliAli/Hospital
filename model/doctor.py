from model.user import User


class Doctor(User):

    def show_menu(self, db):
        super().show_menu(db)
        print("1 - show schedule")
