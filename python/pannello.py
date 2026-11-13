class PannelloFotovoltaico:
    
    def _init_(self, codice: str, modello: str, potenza_kw: float) -> None:
        self.codice = codice
        self.modello = modello
        self.potenza_kw = potenza_kw
    
    def _str_(self) -> str:
        return f"codice impianto: {self.codice}, modello: {self.modello}, potenza: {self.potenza}"
    