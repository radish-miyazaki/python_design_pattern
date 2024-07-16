from __future__ import annotations
import copy
from abc import ABCMeta, abstractmethod


class ItemPrototype(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.__name = name
        self.__review: list[str] = []

    def __str__(self):
        return f"{self.__name}: {self.__review}"

    def set_review(self, review: str):
        self.__review.append(review)

    @abstractmethod
    def create_copy(self) -> ItemPrototype:
        pass


class DeepCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.deepcopy(self)


class ShallowCopyItem(ItemPrototype):
    def create_copy(self) -> ItemPrototype:
        return copy.copy(self)


class ItemManage:
    def __init__(self):
        self.items = {}

    def register_items(self, key: str, item: ItemPrototype):
        self.items[key] = item

    def create(self, key: str) -> ItemPrototype:
        if key in self.items:
            return self.items[key].create_copy()

        raise Exception("指定されたキーが存在しません")


if __name__ == "__main__":
    mouse = DeepCopyItem("マウス")
    keyboard = ShallowCopyItem("キーボード")

    manager = ItemManage()
    manager.register_items("mouse", mouse)
    manager.register_items("keyboard", keyboard)

    cloned_mouse = manager.create("mouse")
    cloned_keyboard = manager.create("keyboard")

    cloned_mouse.set_review("Good!")
    cloned_keyboard.set_review("SoSo!")

    print("mouse (original): ", mouse)
    print("mouse (copy): ", cloned_mouse)

    print("keyboard (original)", keyboard)
    print("keyboard (copy)", cloned_keyboard)
