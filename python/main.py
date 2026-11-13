from pannello import PannelloFotovoltaico
from impianto import ImpiantoSolare

def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare) -> None:
    for i in impianti:
        if i.codice == impianto.codice:
            raise ValueError("Impianto gia presente")
    impianti.append(impianto)
    
def cerca_impianto(impianti: list[ImpiantoSolare], codice: str) -> ImpiantoSolare:
    for i in impianti:
        if i.codice == codice:
            return i
    return None

def riepilogo_impianti(nome_azienda: str, impianti: list[ImpiantoSolare]) -> None :
    for i in impianti:
        print(str(i))

def main() -> None:
    impianti: list[ImpiantoSolare] = []
    
    registra_impianto(impianti, ImpiantoSolare("abcd", "Brandux67", "Napoli", 12, "in installazione"))
    registra_impianto(impianti, ImpiantoSolare("efgh", "Corbi67", "Venezia", 14, "in collaudo"))
    registra_impianto(impianti, ImpiantoSolare("ijkl", "Braso67", "Roma", 16, "attivo"))
    registra_impianto(impianti, ImpiantoSolare("mnop", "Chiucchi67", "Milano", 18, "in installazione"))
    
    impianti[0].aggiungi_pannello(PannelloFotovoltaico("ab", "a67", 2))
    impianti[0].aggiungi_pannello(PannelloFotovoltaico("cd", "b67", 4))
    impianti[1].aggiungi_pannello(PannelloFotovoltaico("ef", "c67", 6))
    impianti[1].aggiungi_pannello(PannelloFotovoltaico("gh", "d67", 8))
    impianti[2].aggiungi_pannello(PannelloFotovoltaico("ij", "e67", 10))
    impianti[2].aggiungi_pannello(PannelloFotovoltaico("kl", "f67", 12))
    impianti[3].aggiungi_pannello(PannelloFotovoltaico("mn", "g67", 14))
    impianti[3].aggiungi_pannello(PannelloFotovoltaico("op", "h67", 16))
    riepilogo_impianti("BranduxInc", impianti)
    cerca_impianto(impianti, "abcd")
    cerca_impianto(impianti, "brandux")
    
if _name_ == "_main_":
    main()





