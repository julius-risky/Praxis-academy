class orang: 
    def __init__(self,nama,nim):
        self.nm = nama
        self.np = nim
    def tampilkan(self):
        print ("nama:", self.nm,"\nnim:", self.np)
class mahasiswa(orang):
    pass

orang=orang("juki", "161414099")
orang.tampilkan()

andi=mahasiswa("andi","161414515")
andi.tampilkan()