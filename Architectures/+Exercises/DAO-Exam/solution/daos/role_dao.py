from abc import ABC, abstractmethod
from ..dtos.role_dto import RoleDTO

class RoleDAO(ABC):

    @abstractmethod
    def get_role_by_id(self, role_id: int) -> RoleDTO:
        pass
