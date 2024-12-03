from ..role_dto import RoleDTO

class RoleToRoleDTOConverter:

    def convert_role_name_to_dto(self, role_name: str) -> RoleDTO:
        role_dto = RoleDTO()
        role_dto.name = role_name
        return role_dto