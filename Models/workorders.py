from Models.Model import Model

class workorders(Model):
    __nameTable = 'workorders'
    __WorkOrderID = 'WorkOrderID'
    __ProductCode = 'ProductCode'
    __OrderDate = 'OrderDate'
    __Deadline = 'Deadline'
    __Quantity = 'Quantity'

    def get(self):
        return super().get(self.__nameTable)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)

    def delete(self,id):
        super().delete(self.__nameTable,id)

    def update(self,table,field,id,values):
        super().update(self.__nameTable, field, values, id)

    def getWorkOrderDate(self, first_date, last_date):
        return super().getWorkOrderDate(first_date,last_date)
