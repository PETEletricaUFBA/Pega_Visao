from dataclasses import dataclass

@dataclass
class PETiano:

    index: int
    name: str
    surname: str
    status: str = "Ativo"
    cartao: bytearray = 0


eu = PETiano(0, "Joelton", "D. Junior", cartao=1)
eu.index = 4
print(eu)