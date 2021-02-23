class Date:
    @classmethod
    def cl_met(cls, date):
        lst = date.split("-")
        return lst

    @staticmethod
    def st_met(date):
        day = int(date[0])
        mes = int(date[1])
        year = int(date[2])
        if day > 31 or day < 1:
            print("неправильно введена дата")
        if mes < 1 or mes > 12:
            print("неправильно введена дата")
        if year > 2022 or year < 2000:
            print("непрвильно введена дата")


a = input("введите дату в формате день-месяц-год: ")
Date.st_met(Date.cl_met(a))
