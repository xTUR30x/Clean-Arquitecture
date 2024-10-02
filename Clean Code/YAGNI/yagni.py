#YAGNI Principle

#Problem

class MessageApp:

    def __init__(self) -> None:
        self.messages = []

    def send_message(self, message:str) -> None:
        self.messages.append(message)
        print(message)

    def recive_message(self) -> None:
        if len(self.messages) > 0:
            return self.messages[-1]
        else:
            return None
        
    def delete_message(self, message:str) -> None:
        pass

    def send_audio(self) -> None:
        pass


#Solution

class MessageApp:

    def __init__(self) -> None:
        self.messages = []

    def send_message(self, message:str) -> None:
        self.messages.append(message)
        print(message)

    def recive_message(self) -> None:
        if len(self.messages) > 0:
            return self.messages[-1]
        else:
            return None