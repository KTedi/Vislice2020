STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'S'
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'  

ZMAGA = 'W'
PORAZ = 'X' 

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper() #geslo znotraj tega objekta bo vedno zapisano z velikimi črkami
        self.crke = [] if crke is None else [crka.upper() for crka in crke] # self.crke = [crka.upper() for crka in crke] - izpeljani seznam

        def napacne_crke(self): #metoda znotraj razreda - ne pozabi na self!
            return [crka for crka in self.crke if crka not in self.geslo] #z izpeljanim seznamom
        
        def pravilne_crke(self):
            return [crka for crka in self.crke if crka in self.geslo]

        def stevilo_napak(self):
            return len(self.napacne_crke())

        def poraz(self):
            return self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK

        def zmaga(self):
            #return set(self.geslo) == set(selfapravilne_crke())
            #return all(crka in self.crke for crka in self.geslo)
            for crka in self.geslo:
                if crka not in self.crke:
                    return False
            return True

        def pravilni_del_gesla(self):
            s = ''
            for crka in self.geslo:
                s += crka if crka in self.crke else '_'
            return s
        
        def nepravilni_ugibi(self):
            return ' '.join(self.napacne_crke())

        def ugibaj(self, ugibana_crka):
            ugibana_crka = ugibana_crka.upper()
            if ugibana_crka in self.crke:
                return PONOVLJENA_CRKA
            else:
                self.crke.append(ugibana_crka)
                if ugibana_crka in self.geslo:
                    if self.zmaga():
                        return ZMAGA
                    else:
                        return PRAVILNA_CRKA
                else:
                    if self.poraz():
                        return PORAZ
                    else:
                        return NAPACNA_CRKA

bazen_besed = []
#to bomo naredili z zanko(naslednja vrstica)
for beseda in open('besede.txt', encoding = 'utf-8'):
    bazen_besed.append(beseda.strip().upper())

def nova_igra():
    beseda = random.choice(bazen_besed)
    return Igra(beseda)


class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()
        self.igre[id_igre] = {igra, ZACETEK}
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra, _ = self.igre[id_igre] #podčrtaj - tega v resnici nikoli ne bomo uporabljali
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = {igra, stanje}
        

