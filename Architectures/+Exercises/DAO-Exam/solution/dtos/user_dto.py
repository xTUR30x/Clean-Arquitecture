from .role_dto import RoleDTO

class UserDTO:

    # Getter y Setter para _id
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    # Getter y Setter para _first_name
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        self._first_name = value

    # Getter y Setter para _last_name
    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        self._last_name = value

    # Getter y Setter para _email
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    # Getter y Setter para _password
    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    # Getter y Setter para role
    @property
    def role(self) -> RoleDTO:
        return self._role

    @role.setter
    def role(self, value: RoleDTO) -> None:
        self._role = value

    # Getter y Setter para money
    @property
    def money(self) -> float:
        return self._money

    @money.setter
    def money(self, value: float) -> None:
        self._money = value

    # Getter y Setter para credit_card
    @property
    def credit_card(self) -> str:
        return self._credit_card

    @credit_card.setter
    def credit_card(self, value: str) -> None:
        self._credit_card = value