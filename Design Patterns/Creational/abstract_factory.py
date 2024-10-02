from abc import ABC, abstractmethod
from typing import List

class Button(ABC):
    @abstractmethod
    def on_click(self) -> None:
        pass

class Textfield(ABC):
    @abstractmethod
    def show_text(self) -> None:
        pass

class CancelButton(Button):
    def on_click(self) -> None:
        print("Cancel button clicked")

class ConfirmButton(Button):
    def on_click(self) -> None:
        print("Confirm button clicked")

class WarningTextfield(Textfield):
    def show_text(self) -> None:
        print("Warning! Textfield")

class SuccessTextfield(Textfield):
    def show_text(self) -> None:
        print("Success! Textfield")



class GUIFactory(ABC):
    @abstractmethod
    def create_cancel_button(self, count: int = 1) -> List[Button]:
        pass

    @abstractmethod
    def create_confirm_button(self, count: int = 1) -> List[Button]:
        pass

    @abstractmethod
    def create_warning_textbox(self) -> Textfield:
        pass

    @abstractmethod
    def create_success_textbox(self) -> Textfield:
        pass

class AdminPageFactory(GUIFactory):
    def create_cancel_button(self, count: int = 1) -> List[Button]:
        return [CancelButton() for _ in range(count)]
    
    def create_confirm_button(self, count: int = 1) -> List[Button]:
        return [ConfirmButton() for _ in range(count)]
    
    def create_success_textbox(self) -> Textfield:
        return SuccessTextfield()
    
    def create_warning_textbox(self) -> Textfield:
        return WarningTextfield()

class UserPageFactory(GUIFactory):
    def create_cancel_button(self, count: int = 1) -> List[Button]:
        return [CancelButton() for _ in range(count)]
    
    def create_confirm_button(self, count: int = 1) -> List[Button]:
        return [ConfirmButton() for _ in range(count)]
    
    def create_success_textbox(self) -> Textfield:
        return SuccessTextfield()
    
    def create_warning_textbox(self) -> Textfield:
        return WarningTextfield()

class GUIBuilder:

    def build_components(self, factory: GUIFactory, cancel_count: int, confirm_count: int) -> None:
        cancel_buttons = factory.create_cancel_button(cancel_count)
        confirm_buttons = factory.create_confirm_button(confirm_count)

        warning_textbox = factory.create_warning_textbox()
        success_textbox = factory.create_success_textbox()

        for button in cancel_buttons:
            button.on_click()
        
        for button in confirm_buttons:
            button.on_click()
        
        warning_textbox.show_text()
        success_textbox.show_text()

if __name__ == "__main__":
    builder = GUIBuilder()

    page_type = {
        "admin": AdminPageFactory(),
        "user": UserPageFactory()
    }

    selected_type = 'admin'

    for page in page_type:
        if selected_type == page:
            builder.build_components(page_type[page], 2, 1)