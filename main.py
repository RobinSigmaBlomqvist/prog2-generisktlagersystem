from typing import Generic, TypeVar

T = TypeVar("T")  # Typvariabel


class Lager(Generic[T]):
    def __init__(self, namn: str):
        self.namn = namn  # Instansvariabel
        self.innehall: list[T] = []  # Instansvariabel

    def lagg_till(self, vara: T) -> None:
        self.innehall.append(vara)  # Parameter/variabel i metoden

    def visa_innehall(self) -> list[T]:
        return self.innehall.copy()  # Lokal variabel returneras


if __name__ == "__main__":
    bok_lager = Lager[str]("Böcker")  # Instansvariabel
    bok_lager.lagg_till("Python")  # Parameter i lagg_till
    bok_lager.lagg_till("Databaser")  # Parameter i lagg_till

    print(bok_lager.visa_innehall())
