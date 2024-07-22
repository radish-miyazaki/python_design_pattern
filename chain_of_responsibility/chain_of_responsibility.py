from __future__ import annotations
from abc import ABCMeta, abstractmethod
import re


class ValidationHandler(metaclass=ABCMeta):
    def __init__(self):
        self.__next_handler = None

    def set_handler(self, handler: ValidationHandler) -> ValidationHandler:
        self.__next_handler = handler
        return handler

    def validate(self, input: str) -> bool:
        result = self._exec_validation(input)

        if not result:
            self._get_error_message()
            return False

        if self.__next_handler:
            return self.__next_handler.validate(input)

        return True


    @abstractmethod
    def _exec_validation(self, input: str) -> bool:
        pass

    @abstractmethod
    def _get_error_message(self):
        pass


class NotNullValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        result = False
        if input:
            result = True

        print(f"NotNullValidationHandler の結果: {result}")
        return result

    def _get_error_message(self):
        print("何も入力されていません")


class AlphabetValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        reg = re.compile("^[a-zA-Z]+$")
        result = bool(re.search(reg, input))
        print(f"AlphabetValidationHandler の結果: {result}")
        return result

    def _get_error_message(self):
        print("半角英字で入力してください")


class MinLengthValidationHandler(ValidationHandler):
    def _exec_validation(self, input: str) -> bool:
        result = len(input) >= 8
        print(f"MinLengthValidationHandler の結果: {result}")
        return result

    def _get_error_message(self):
        print("8文字以上で入力してください")


if __name__ == "__main__":
    not_null_handler = NotNullValidationHandler()
    alphabet_handler = AlphabetValidationHandler()
    min_length_handler = MinLengthValidationHandler()

    # not_null -> alphabet -> min_length
    not_null_handler.set_handler(alphabet_handler).set_handler(min_length_handler)

    # result = not_null_handler.validate("")
    # result = not_null_handler.validate("1")
    # result = not_null_handler.validate("h")
    result = not_null_handler.validate("helloworld")
    if result:
        print("すべてのバリデーションに通過しました")
