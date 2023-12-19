import mysql.connector

def execute_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='DBT12',
            user='root',
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Задание 1: Для выбранного цеха, выдать список операций, выполняемых им
def get_workshop_operations(connection, workshop_number):
    query = '''
        SELECT O.OperationID, O.OperationDescription, M.MaterialCode, M.MaterialQuantity
        FROM Operations O
        JOIN MaterialUsage M ON O.OperationID = M.OperationID
        WHERE O.WorkshopNumber = %s
    '''
    params = (workshop_number,)
    result = execute_query(connection, query, params)
    print(f"Список операций для цеха {workshop_number}:")
    print(result)

# Задание 2: Показать список инструментов и предоставить возможность добавления нового
def list_and_add_tools(connection):
    # Показать список инструментов
    query_show = '''
        SELECT ToolID, ToolDescription
        FROM Tools
    '''
    result_show = execute_query(connection, query_show)
    print("Список инструментов:")
    print(result_show)

    # Добавить новый инструмент
    new_tool_description = 'New Tool'
    query_add = '''
        INSERT INTO Tools (ToolDescription)
        VALUES (%s)
    '''
    params_add = (new_tool_description,)
    execute_query(connection, query_add, params_add)

# Задание 3: Вывести список используемых инструментов
def list_used_tools(connection):
    query = '''
        SELECT DISTINCT T.ToolID, T.ToolDescription
        FROM Operations O
        JOIN ToolUsage TU ON O.OperationID = TU.OperationID
        JOIN Tools T ON TU.ToolID = T.ToolID
    '''
    result = execute_query(connection, query)
    print("Список используемых инструментов:")
    print(result)

# Задание 4: Для указанного интервала дат, вывести список нарядов
def list_work_orders_by_date(connection, start_date, end_date):
    query = '''
        SELECT WorkOrderID, OrderDate, ProductCode, RequiredQuantity
        FROM WorkOrders
        WHERE OrderDate BETWEEN %s AND %s
    '''
    params = (start_date, end_date)
    result = execute_query(connection, query, params)
    print(f"Список нарядов за период с {start_date} по {end_date}:")
    print(result)

# Задание 5: Показать список операций и предоставить возможность добавления новой операции
def list_and_add_operations(connection):
    # Показать список операций
    query_show = '''
        SELECT OperationID, OperationDescription
        FROM Operations
    '''
    result_show = execute_query(connection, query_show)
    print("Список операций:")
    print(result_show)

    # Добавить новую операцию
    new_operation_description = 'New Operation'
    query_add = '''
        INSERT INTO Operations (OperationDescription)
        VALUES (%s)
    '''
    params_add = (new_operation_description,)
    execute_query(connection, query_add, params_add)

# Задание 6: Вывести список расходуемых материалов, используемых в различных нарядах
def list_materials_used_in_work_orders(connection):
    query = '''
        SELECT DISTINCT M.MaterialCode, M.MaterialDescription
        FROM WorkOrders WO
        JOIN MaterialUsage M ON WO.WorkOrderID = M.WorkOrderID
    '''
    result = execute_query(connection, query)
    print("Список расходуемых материалов, используемых в нарядах:")
    print(result)

# Задание 7: Вывести список товаров, с указанием используемых инструментов
def list_products_with_tools(connection):
    query = '''
        SELECT DISTINCT P.ProductCode, P.ProductDescription, T.ToolID, T.ToolDescription
        FROM WorkOrders WO
        JOIN Products P ON WO.ProductCode = P.ProductCode
        JOIN Operations O ON P.ProductCode = O.ProductCode
        JOIN ToolUsage TU ON O.OperationID = TU.OperationID
        JOIN Tools T ON TU.ToolID = T.ToolID
    '''
    result = execute_query(connection, query)
    print("Список товаров с указанием используемых инструментов:")
    print(result)

# Задание 8: Показать список нарядов и предоставить возможность добавления нового
def list_and_add_work_orders(connection):
    # Показать список нарядов
    query_show = '''
        SELECT WorkOrderID, OrderDate, ProductCode, RequiredQuantity
        FROM WorkOrders
    '''
    result_show = execute_query(connection, query_show)
    print("Список нарядов:")
    print(result_show)

    # Добавить новый наряд
    new_order_date = '2023-01-20'
    new_product_code = 'PRO456'
    new_required_quantity = 50
    query_add = '''
        INSERT INTO WorkOrders (OrderDate, ProductCode, RequiredQuantity)
        VALUES (%s, %s, %s)
    '''
    params_add = (new_order_date, new_product_code, new_required_quantity)
    execute_query(connection, query_add, params_add)

# Задание 9: Вывести отчет о производстве товаров различными цехами
def production_report_by_workshops(connection):
    query = '''
        SELECT O.WorkshopNumber, P.ProductCode, P.ProductDescription, SUM(WO.RequiredQuantity) as ProducedQuantity
        FROM WorkOrders WO
        JOIN Operations O ON WO.ProductCode = O.ProductCode
        JOIN Products P ON WO.ProductCode = P.ProductCode
        GROUP BY O.WorkshopNumber, P.ProductCode, P.ProductDescription
    '''
    result = execute_query(connection, query)
    print("Отчет о производстве товаров различными цехами:")
    print(result)

# Подключаемся к базе данных
connection = connect_to_database()

if not connection:
    print("Не удалось подключиться к базе данных.")
else:
    try:
        # Задание 1
        workshop_number = 1
        get_workshop_operations(connection, workshop_number)

        # Задание 2
        list_and_add_tools(connection)

        # Задание 3
        list_used_tools(connection)

        # Задание 4
        start_date = '2023-01-10'
        end_date = '2023-01-15'
        list_work_orders_by_date(connection, start_date, end_date)

        # Задание 5
        list_and_add_operations(connection)

        # Задание 6
        list_materials_used_in_work_orders(connection)

        # Задание 7
        list_products_with_tools(connection)

        # Задание 8
        list_and_add_work_orders(connection)

        # Задание 9
        production_report_by_workshops(connection)

    except Exception as e:
        print(f"Error: {e}")

    # Закрываем соединение с базой данных
    connection.close()
