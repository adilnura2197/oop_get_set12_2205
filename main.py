class Mahsulot:
    def __init__(self, nom, son):
        self.nom = nom
        self.__son = son

    def get_son(self):
        return self.__son

    def set_son(self, son):
        if son >= 0:
            self.__son = son
            print("Soni yangilandi")
        else:
            print("Xato qiymat")


m1 = Mahsulot("Olma", 50)
print(m1.get_son())
