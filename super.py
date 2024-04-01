class person:
    country = "india"
    def __init__(self) -> None:
        pass

    def readramayan(self):
        print("i am reading ramayan...")

class reader(person):
    occupation = "reading"

    def getmantra(self):
        super().readramayan()
        print("reader is reading mantra....")

    def readramayan(self):
        super().readramayan()
        print("i am a reader now i am reading ramayan...")

class pandit(reader):
    occupation = "chanting"

    def chantinghareram(self):
        print(f"pandit is chanting harerama harekrishna...  ")

    def readramayan(self):
        super().readramayan()
        print("i am reading ramayan...")

p = person()
p.readramayan()

r = reader()
r.readramayan()

pd = pandit()
pd.readramayan()


