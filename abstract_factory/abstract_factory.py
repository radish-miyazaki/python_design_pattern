from abc import ABCMeta, abstractmethod


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass


class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self):
        pass


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsCheckbox(Checkbox):
    def switch(self):
        print('Windows のチェックボックスが切り替えられました')


class WindowsButton(Button):
    def press(self):
        print('Windows のボタンが押されました')


class WindowsGUIFactory(GUIFactory):
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_button(self) -> Button:
        return WindowsButton()


class MacCheckbox(Checkbox):
    def switch(self):
        print('Mac のチェックボックスが切り替えられました')


class MacButton(Button):
    def press(self):
        print('Mac のボタンが押されました')


class MacGUIFactory(GUIFactory):
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

    def create_button(self) -> Button:
        return MacButton()


def run(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.press()
    checkbox.switch()


if __name__ == '__main__':
    windows_gui_factory = WindowsGUIFactory()
    mac_gui_factory = MacGUIFactory()
    run(windows_gui_factory)
    run(mac_gui_factory)
