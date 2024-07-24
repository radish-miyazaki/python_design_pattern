from abc import ABC, abstractmethod


# Implementor
class MessageApp(ABC):
    @abstractmethod
    def send(self):
        pass


class LINE(MessageApp):
    def send(self):
        print("LINE でメッセージを送信しました")


class X(MessageApp):
    def send(self):
        print("X でメッセージを送信しました")


class Facebook(MessageApp):
    def send(self):
        print("Facebook でメッセージを送信しました")


# Abstraction
class OS(ABC):
    def __init__(self):
        self._app = None

    def set_app(self, app: MessageApp):
        self._app = app

    @abstractmethod
    def send_message(self):
        pass


class IOS(OS):
    def send_message(self):
        print("iOS でメッセージ送信")
        if self._app is None:
            raise Exception("アプリが指定されていません")

        self._app.send()


class Android(OS):
    def send_message(self):
        print("Android でメッセージ送信")
        if self._app is None:
            raise Exception("アプリが指定されていません")

        self._app.send()


if __name__ == "__main__":
    line = LINE()
    x = X()
    facebook = Facebook()

    ios = IOS()
    android = Android()

    ios.set_app(line)
    ios.send_message()
    android.set_app(facebook)
    android.send_message()
