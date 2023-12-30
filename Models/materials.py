from Models.Model import Model

class materials(Model):
    __nameTable = 'materials'
    __MaterialCode = 'MaterialCode'
    __Code_Class = 'Code_Class'
    __MaterialName = 'MaterialName'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)

    def getOneRow(self, id):
        return super().getOneRow(self.__nameTable,id)