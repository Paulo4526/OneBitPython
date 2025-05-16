from smartphone_filho import Smartphone
from phone_pai import Phone
class main():
    tel = Phone("Samsung", "S10", "Galaxy", "2800")
    print(tel)
    tel.make_a_call(11951069832)
    print(vars(tel))

    smart = Smartphone("Samsung", "S10", "Galaxy", "2800", "128", "1", "200")
    smart.show_details()
    print(vars(smart))

if __name__ == '__main__':
    main()