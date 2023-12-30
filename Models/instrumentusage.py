from Models.Model import Model

class instrumentusage(Model):
    __nameTable = 'instrumentusage'
    __OperationID = 'OperationID'
    __InstrumentID = 'InstrumentID'
    __UsedQuantity = 'UsedQuantity'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)