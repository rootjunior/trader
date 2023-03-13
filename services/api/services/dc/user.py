from dataclasses import dataclass


@dataclass
class UserDTO:
    id: int
    name: str
    balance: float
