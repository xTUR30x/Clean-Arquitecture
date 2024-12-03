from typing import List
from .role_to_DTO_converter import RoleDTO
from ..user_dto import UserDTO
from ...entities.user import User

class UserToUserDTOConverter:

    def __init__(self) -> None:
        self._role_converter = RoleDTO()

    def convert_user_id_to_dto(self, user_id: int) -> UserDTO:
        user_dto = UserDTO()
        user_dto.name = user_id
        return user_dto
    
    def convert_dto_to_user(self, userDTO: UserDTO) -> User:
        user = User()
        user.first_name = userDTO.first_name
        user.last_name = userDTO.last_name
        user.role = self._role_converter.convert_dto_to_role(userDTO.role)
        user.password = userDTO.password
        user.email = userDTO.email
        user.money = userDTO.money
        user.credit_card = userDTO.credit_card

        return user
    
    def convert_all_userDTOs_to_users(self, userDtos : List[UserDTO]) -> List[User]:
        users = []
        
        for dto in userDtos:
            users.append(self.convert_dto_to_user(dto))

        return users