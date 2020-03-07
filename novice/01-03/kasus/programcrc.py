class biodata: 
    def __init__(self,nama,nim,email,univ):
        self.nm = nama
        self.np = nim
        self.em = email
        self.un = univ
    def tampilkan(self):
        print ("nama:", self.nm,"\nnim:", self.np,"\nemail:",self.em,"\nuniv",self.un)
class mahasiswa(biodata):
    pass

biodata=biodata("juki", "161414099","julius.risky@gmail.com","universitas sanata dharma")
biodata.tampilkan()