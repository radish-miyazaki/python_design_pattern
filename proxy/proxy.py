from abc import ABC, abstractmethod


class Server(ABC):
    @abstractmethod
    def handle(self, user_id: str):
        pass


class Proxy(Server):
    def __init__(self, server: Server):
        self.__server = server

    def _authorize(self, user_id: str):
        authorized_user_id = ["1", "2", "3"]

        if not user_id in authorized_user_id:
            raise Exception("操作が許可されていません")

    def handle(self, user_id: str):
        self._authorize(user_id)
        print("処理を開始します")  # 前処理
        self.__server.handle(user_id)
        print("処理が終了しました")  # 後処理


class RealServer(Server):
    def handle(self, user_id: str):
        print(f"{user_id} の処理を実行中...")


if __name__ == "__main__":
    server = RealServer()
    proxy = Proxy(server)
    proxy.handle("1")
    # proxy.handle("5")
