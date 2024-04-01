class person:
    country = "india"

    def readramayan(self):
        print("i am reading ramayan...")

class reader(person):
    occupation = "reading"

    def getmantra(self):
        print("reader is {self.mantra}....")

    def readramayan(self):
        print("i am a reader now i am reading ramayan...")

class pandit(reader):
    occupation = "chanting"

    def chantinghareram(self):
        print(f"pandit is chanting harerama harekrishna...  ")

    def readramayan(self):
        print("i am reading ramayan...")

p = person()
p.readramayan()
r = reader()
r.getmantra()
pd = pandit()
pd.chantinghareram()
print(pd.occupation)
print(pd.country)

