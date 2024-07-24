class Stamp:
    def __init__(self, char: str):
        self.__char = char

    def print_char(self):
        print(self.__char)


class StampFactory:
    __pool: dict[str, Stamp]

    def __init__(self):
        self.__pool = {}

    def get_stamp(self, char: str) -> Stamp:
        stamp = self.__pool.get(char)
        if stamp:
            return stamp

        new_stamp = Stamp(char)
        self.__pool[char] = new_stamp
        return new_stamp

    def get_pool(self) -> dict[str, Stamp]:
        return self.__pool


if __name__ == "__main__":
    factory = StampFactory()
    stamp1 = factory.get_stamp("し")
    stamp2 = factory.get_stamp("ん")
    stamp3 = factory.get_stamp("ぶ")
    stamp4 = factory.get_stamp("ん")
    stamp5 = factory.get_stamp("し")

    stamp1.print_char()
    stamp2.print_char()
    stamp3.print_char()
    stamp4.print_char()
    stamp5.print_char()

    print(factory.get_pool())
