from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: list[str]
    hobbies: list[str]
    picture: str
    address: str
    state: str
    city: str
