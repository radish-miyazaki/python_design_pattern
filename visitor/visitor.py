from __future__ import annotations
from abc import ABC, abstractmethod


class Entry(ABC):
    def __init__(self, code: str, name: str) -> None:
        self.__code = code
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @abstractmethod
    def get_children(self) -> list[Entry]:
        pass

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Group(Entry):
    def __init__(self, code: str, name: str) -> None:
        super().__init__(code, name)
        self.__entries: list[Entry] = []

    def add(self, entry: Entry):
        self.__entries.append(entry)

    def get_children(self) -> list[Entry]:
        return self.__entries

    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Employee(Entry):
    def __init__(self, code: str, name: str) -> None:
        super().__init__(code, name)

    def get_children(self) -> list[Entry]:
        return []

    def accept(self, visitor: Visitor):
        visitor.visit(self)


class Visitor(ABC):
    @abstractmethod
    def visit(self, entry: Entry):
        pass


class ListVisitor(Visitor):
    def visit(self, entry: Entry):
        if type(entry) == Group:
            print(f"{entry.code}: {entry.name}")
        else:
            print(f"  {entry.code}: {entry.name}")

        for child in entry.get_children():
            child.accept(self)


class CountVisitor(Visitor):
    def __init__(self) -> None:
        self.__group_count = 0
        self.__employee_count = 0

    @property
    def group_count(self) -> int:
        return self.__group_count

    @property
    def employee_count(self) -> int:
        return self.__employee_count

    def visit(self, entry: Entry):
        if type(entry) == Group:
            self.__group_count += 1
        else:
            self.__employee_count += 1

        for child in entry.get_children():
            child.accept(self)


if __name__ == '__main__':
    root_entry = Group("01", "本社")
    root_entry.add(Employee("001", "社長"))
    root_entry.add(Employee("002", "副社長"))

    group1 = Group("10", "神奈川支部")
    group1.add(Employee("1001", "支部長"))

    group2 = Group("11", "横浜営業所")
    group2.add(Employee("1101", "営業部長"))
    group2.add(Employee("1102", "山田さん"))
    group2.add(Employee("1102", "鈴木さん"))
    group2.add(Employee("1102", "田中さん"))

    group1.add(group2)
    root_entry.add(group1)

    list_visitor = ListVisitor()
    count_visitor = CountVisitor()

    root_entry.accept(list_visitor)
    root_entry.accept(count_visitor)

    print(f"グループ数: {count_visitor.group_count}")
    print(f"社員数: {count_visitor.employee_count}")
