from model.user import User


def cancel_appointment():
    pass


def send_pm():
    pass


def show_schedule():
    pass


class Doctor(User):

    def show_menu(self, db):
        super().show_menu(db)
        print("1 - show schedule")
        print("2 - send PM to a patient")
        print("3 - cancel an appointment")
        choice = int(input())
        if choice == 1:
            show_schedule()
        elif choice == 2:
            send_pm()
        elif choice == 3:
            cancel_appointment()
