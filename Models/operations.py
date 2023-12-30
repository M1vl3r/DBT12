from Models.Model import Model

class operations(Model):
    __nameTable = 'operations'
    __Description = 'Description'
    __AvgDuration = 'AvgDuration'
    __DrawingNumber = 'DrawingNumber'
    __WorkshopNumber = 'WorkshopNumber'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)

    def add(self):
        Description = input("Введите описание операции: ")
        AvgDuration = input("Введите среднюю продолжительность операции: ")
        DrawingNumber = input("Укажите чертеж который использовался: ")
        WorkshopNumber = input("Укажите цех на котором производилиась операция: ")
        str = f"{self.__Description}, {self.__AvgDuration},{self.__DrawingNumber},{self.__WorkshopNumber}"
        super().add(self.__nameTable, str, Description,AvgDuration,DrawingNumber,WorkshopNumber)