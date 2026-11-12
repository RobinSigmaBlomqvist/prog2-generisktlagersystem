from typing import Generic, TypeVar

T = TypeVar("T")  # Global

class Lager(Generic[T]):
    antal_objekt = 0  # Klass
    totalt_lagda_varor = 0  # Klass
    def __init__(self, namn: str):
        self.namn = namn  # Instans
        self.innehall: list[T] = []  # Instans
        self.max_kapacitet = 100  # Instans
        Lager.antal_objekt += 1  # Klass

    def lagg_till(self, vara: T) -> None:
        ny_vara = vara  # Lokal
        self.innehall.append(ny_vara)  # Instans
        Lager.totalt_lagda_varor += 1  # Klass

    def visa_innehall(self) -> list[T]:
        kopia = self.innehall.copy()  # Lokal
        return kopia  # Lokal

    def demo_nastlad_funktion(self) -> str:
        meddelande = "Lagerstatus"  # Lokal
        def skriv_status() -> str:
            return f"{meddelande}: {self.namn} innehåller {len(self.innehall)} föremål."  # Enclosing

        return skriv_status()  # Lokal

if __name__ == "__main__":
    bok_lager = Lager[str]("Böcker")  # Instans
    cd_lager = Lager[str]("CD-skivor")  # Instans

    bok_lager.lagg_till("Python")  # Parameter
    bok_lager.lagg_till("Databaser")  # Parameter
    cd_lager.lagg_till("Rock")  # Parameter

    print(bok_lager.visa_innehall())  # Lokal
    print(bok_lager.demo_nastlad_funktion())  # Enclosing
    print(f"Totalt skapade lager: {Lager.antal_objekt}")  # Klass
    print(f"Totalt lagda varor: {Lager.totalt_lagda_varor}")  # Klass
