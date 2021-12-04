import string
import psycopg2


def predict(mes: string, dia: string) -> any:
    CERRADO = execute_query(
        """ SELECT count(*) FROM history_park WHERE fecha ilike '%""" + dia + """/""" + mes + """/2%' AND estado_parque = 'CERRADO'; """)
    ABIERTO = execute_query(
        """ SELECT count(*) FROM history_park WHERE fecha ilike  '%""" + dia + """/""" + mes + """/2%' AND estado_parque = 'ABIERTO'; """)
    PARCIAL = execute_query(
        """ SELECT count(*) FROM history_park WHERE fecha ilike  '%""" + dia + """/""" + mes + """/2%' AND estado_parque = 'PARCIAL'; """)

    print("Cerrado: " + str(CERRADO))
    print("Abierto: " + str(ABIERTO))
    print("Parcial: " + str(PARCIAL))

    if CERRADO > ABIERTO and CERRADO > PARCIAL:
        print(" Ese dia debe estar Cerrado")
    elif ABIERTO > PARCIAL and ABIERTO > CERRADO:
        print("ese dia debe estar abierto")
    elif PARCIAL > ABIERTO and PARCIAL > CERRADO:
        print("ese dia es parcial")
    else:
        print("")

def execute_query(query) -> any:
    connection = psycopg2.connect(user="postgres",
                                  password="Udel$2021$1808Udel",
                                  host="159.89.129.181",
                                  port="8934",
                                  database="aplicacion_demostracion")
    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchone()
    return record[0]


mes = input("mes: ")
dia = input("dia: ")

predict(mes=mes, dia=dia)
