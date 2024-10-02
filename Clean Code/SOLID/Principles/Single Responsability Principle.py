#Single Responsability Principle

#Problem

from enum import Enum

class Role(Enum):
    ADMIN = 1, 
    MANAGER = 2, 
    DEVELOPER = 3,

class User:
    def __init__(self, id:int, primary_email:str, secundary_email:str, role: Role) -> None:
        self.id = id
        self.primaryEmail = primary_email
        self.secundaryEmail = secundary_email
        self.role = role

    def set_secundaryEmail(self, secundaryEmail:str) -> None:
        self.secundaryEmail = secundaryEmail

    def get_role(self) -> Role:
        return self.role
    
    def sendMoney(self, user, amount:int) -> None:
        print("Sending money...")


class MailboxSettingsService:

    #Tiene mas de una sola responsabilidad

    def changeSecundaryEmail(self, user:User, secundary_email:str) -> None:
        if self.hasAccess(user):
            user.set_secundaryEmail(secundary_email)

    def hasAccess(self, user:User) -> bool:
        if user.get_role() == Role.ADMIN:
            return True
        else:
            return False
        
if __name__ == "__main":
    mailbox_settings_service = MailboxSettingsService()
    user = User()
    user2 = User()

    #Primera responsabilidad 
    mailbox_settings_service.changeSecundaryEmail(user, 'new@mail.com')

    #Segunda responsabilidad
    if mailbox_settings_service.hasAccess(user):
        user.sendMoney(user2, 200)



#Solution 

class SecurityService:

    #Ahora esta clase se encarga de la seguridad
    def hasAccess(self, user:User) -> bool:
            if user.get_role() == Role.ADMIN:
                return True
            else:
                return False


class MailboxSettingsService:

    #Ahora esta clase se encarga de gestionar el correo
    def __init__(self, security_service:SecurityService) -> None:
        self.security_service = SecurityService()

    def changeSecundaryEmail(self, user:User, secundary_email:str) -> None:
        if self.hasAccess(user):
            user.set_secundaryEmail(secundary_email)


        
if __name__ == "__main":
    
    mailbox_settings_service = MailboxSettingsService()
    user = User()
    user2 = User()

    #Primera responsabilidad 
    mailbox_settings_service.changeSecundaryEmail(user, 'new@mail.com')

    #Segunda responsabilidad
    if mailbox_settings_service.security_service.hasAccess(user):
        user.sendMoney(user2, 200)

