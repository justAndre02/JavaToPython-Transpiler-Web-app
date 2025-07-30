# Unit test result: ❌ FAILED (see log for details)
class User:
    id: int
    name: str
    email: str

    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int) -> None:
        self.id = id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str) -> None:
        self.email = email

    def __str__(self) -> str:
        return f"User[ID={self.id}, Name='{self.name}', Email='{self.email}']"