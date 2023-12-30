from Models.Model import Model

class group(Model):
    __nameTable = 'group'
    __nameOfGroup = 'nameOfGroup'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable,field)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)

    def add(self):
        nameOfGroup = input("Введите название группы: ")
        str = f"{self.__nameOfGroup}"
        super().add(self.__nameTable, str, nameOfGroup)