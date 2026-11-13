from pannello import PannelloFotovoltaico

class ImpiantoSolare:
    
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli: list[PannelloFotovoltaico] = []
     
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None:
        for p in self.pannelli:
            if p.codice == pannello.codice:
                raise ValueError("Pannello gia presente")
        self.pannelli.append(pannello)
    
    def potenza_pannelli(self) -> float:
        sum = 0
        for p in self.pannelli:
            sum += p.potenza_kw
        return sum
    
    def cerca_pannello(self, codice: str) -> PannelloFotovoltaico:
        for p in self.pannelli
            if p.codice == codice:
                return p
        return None
    
    def rimuovi_pannello(self, codice: str) -> PannelloFotovoltaico:
        for p in self.pannelli:
            if p.codice == codice:
                self.pannelli.remove(p)
                return p
        return None
    
    def pannelli_sotto_potenza(self, potenza_massima: float) -> list[PannelloFotovoltaico]:
        return [self.pannelli for p in self.pannelli if p.potenza_kw <= potenza_massima]