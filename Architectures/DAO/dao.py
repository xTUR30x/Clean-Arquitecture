# Data Access Object Pattern

#DTO
class Client:
    def __init__(self, id: int, nombre: str) -> None:
        self.id = id
        self.nombre = nombre

    def __repr__(self) -> str:
        return f"Client id = {self.id}, nombre = {self.nombre}"
    

class ClientDAO:
    def __init__(self, connection) -> None:
        self.conncetion = connection

    def find_all(self):
        #Database query
        print("getting all users...")


if __name__ == "__main__":
    connection = 'database connection'
    client_dao = ClientDAO(connection)
    client_dao.find_all()