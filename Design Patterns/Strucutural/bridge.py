#Bridge Pattern

from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass
    
    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass

class Television(Device):
    def __init__(self):
        self.volume = 10
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True
        print("Televisor encendido.")

    def disable(self):
        self.enabled = False
        print("Televisor apagado.")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volumen del televisor ajustado a {self.volume}.")

class Radio(Device):
    def __init__(self):
        self.volume = 5
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True
        print("Radio encendida.")

    def disable(self):
        self.enabled = False
        print("Radio apagada.")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Volumen de la radio ajustado a {self.volume}.")


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_up(self):
        new_volume = self.device.volume + 1
        self.device.set_volume(new_volume)

    def volume_down(self):
        new_volume = max(0, self.device.volume - 1)
        self.device.set_volume(new_volume)
    

if __name__ == '__main__':
    tv = Television()
    radio = Radio()

    tv_remote = RemoteControl(tv)
    radio_remote = RemoteControl(radio)

    # Controlando el televisor
    tv_remote.toggle_power() 
    tv_remote.volume_up()     

    # Controlando la radio
    radio_remote.toggle_power()
    radio_remote.volume_down()   