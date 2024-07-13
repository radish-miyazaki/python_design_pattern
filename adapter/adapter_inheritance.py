from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass


class NewLibrary:
    def get_json_data(self) -> list[dict[str, str]]:
        return [
            {
                "data1": "json_dataA",
                "data2": "json_dataB"
            },
            {
                "data1": "json_dataC",
                "data2": "json_dataD"
            }
        ]


class JsonToCsvAdapter(NewLibrary, Target):
    def get_csv_data(self) -> str:
        json_data = self.get_json_data()

        header = ",".join(list(json_data[0].keys())) + "\n"
        body = "\n".join([",".join(data.values()) for data in json_data])

        return header + body


if __name__ == '__main__':
    adaptee = NewLibrary()
    print("=== Adaptee が提供するデータ ===")
    print(adaptee.get_json_data())

    print("")
    adapter = JsonToCsvAdapter()
    print("=== Adapter に変換されたデータ ===")
    print(adapter.get_csv_data())
