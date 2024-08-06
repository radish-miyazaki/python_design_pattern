from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def register_user(self, user: User):
        pass

    @abstractmethod
    def send_message(self, msg: str, send_user: User):
        pass


class ChatRoom(Mediator):
    def __init__(self):
        self.__members: list[User] = []

    def register_user(self, user: User):
        self.__members.append(user)

    def send_message(self, msg: str, send_user: User):
        for member in self.__members:
            if member != send_user:
                member.receive(msg)


class User(ABC):
    def __init__(self, mediator: Mediator, name: str):
        self._mediator = mediator
        self._name = name

    @abstractmethod
    def send(self, msg: str):
        pass

    @abstractmethod
    def receive(self, msg: str):
        pass


class ChatUser(User):
    def send(self, msg: str):
        print(f"{self._name} send: {msg}")
        self._mediator.send_message(msg, self)

    def receive(self, msg: str):
        print(f"{self._name} receive: {msg}")


if __name__ == '__main__':
    chat_room = ChatRoom()

    user1 = ChatUser(chat_room, "User1")
    user2 = ChatUser(chat_room, "User2")
    user3 = ChatUser(chat_room, "User3")

    chat_room.register_user(user1)
    chat_room.register_user(user2)
    chat_room.register_user(user3)

    user1.send("Hello")
    user2.send("Good evening")
