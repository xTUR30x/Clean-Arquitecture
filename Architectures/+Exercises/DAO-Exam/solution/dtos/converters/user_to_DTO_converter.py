from .role_to_DTO_converter import RoleDTO
from ..user_dto import UserDTO

class UserToUserDTOConverter:

    def __init__(self) -> None:
        self._role_converter = RoleDTO()

    def convert_role_name_to_dto(self, category_name: str) -> CategoryDTO:
        category_dto = CategoryDTO()
        category_dto.name = category_name
        return category_dto