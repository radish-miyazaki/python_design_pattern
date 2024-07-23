from abc import ABC, abstractmethod
import datetime


class Component(ABC):
    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class Logger(Component):
    def get_log_message(self, msg: str) -> str:
        return msg


class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def get_log_message(self, msg: str) -> str:
        pass


class TimeStampDecorator(Decorator):
    def get_log_message(self, msg: str) -> str:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        return self._component.get_log_message(f"{timestamp} {msg}")


class LogLevelDecorator(Decorator):
    def __init__(self, component: Component, log_level: str):
        super().__init__(component)
        self.__log_level = log_level

    def get_log_message(self, msg: str) -> str:
        return self._component.get_log_message(f"{self.__log_level}: {msg}")


if __name__ == "__main__":
    logger = Logger()
    log_level_logger = LogLevelDecorator(logger, "INFO")
    timestamp_logger = TimeStampDecorator(log_level_logger)

    print(logger.get_log_message("Design Pattern!"))
    print(log_level_logger.get_log_message("Design Pattern!"))
    print(timestamp_logger.get_log_message("Design Pattern!"))
