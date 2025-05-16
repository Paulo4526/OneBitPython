from hourse import Horse
from lion import Lion

def main():
    cavalo = Horse()
    cavalo.set_name("Aladar")
    cavalo.set_size("200cm")
    cavalo.set_color("Brown")
    cavalo.set_race("Alazão")
    cavalo.show_datails()

    leao = Lion()
    leao.set_name("Simba")
    leao.set_size("150cm")
    leao.set_color("Yellow")
    leao.set_mane("Long Mane")
    leao.show_details()

if __name__ == "__main__":
    main()