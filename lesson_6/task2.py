class Road:
    def __init__(self, lenght, weight):
        self._lenght = lenght
        self._weight = weight

    def raschot(self):

# ааааааа, до меня доперло, что можно ту писать self._lenght, чтобы передавались аргументы экземпляра,
# капец а я так долго думал над первой задачей, а еще я понял зачем нужен __init__, да, вы говрили,
# но тогда я этого не осознавал, а тут на меня снизошло озарение

        print(f"вес необходимого асфальта для асфальтирования вашей дороги равен "
              f"{self._lenght * self._weight * 25 * 5} кг")


a = Road(12, 12)
a.raschot()
