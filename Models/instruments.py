from Models.Model import Model

class instruments(Model):
    __nameTable = 'instruments'
    __InstrumentType = 'InstrumentType'
    __AvailableCount = 'AvailableCount'
    __TotalCount = 'TotalCount'
    __ArrivalDate = 'ArrivalDate'


    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)

    def add(self):
        InstrumentType = input("Введите тип инструмента: ")
        AvailableCount = input("Введите сколько их можно использовать: ")
        TotalCount = input("Введите сколько их всего: ")
        ArrivalDate = input("Введите когда инструмент поступил на склад: ")
        str = f"{self.__InstrumentType}, {self.__AvailableCount},{self.__TotalCount},{self.__ArrivalDate}"
        super().add(self.__nameTable, str, InstrumentType,AvailableCount,TotalCount,ArrivalDate)