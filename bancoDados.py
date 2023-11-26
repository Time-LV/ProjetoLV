import pymysql
import time


class dataBase:
    def __init__(self) -> None:
        pass


def inserirDados(valor):
    conexaoDB = pymysql.connect(host="db4free.net", user="grupo8", password="12341234", database="proj_grupo8")
    cursor = conexaoDB.cursor()
    sql = """INSERT INTO minhaTabela(valores)
            VALUES (%s)"""
    try:
        cursor.execute(sql, valor)
        conexaoDB.commit()  # tornar mudanças permanentes no Banco de Dados

    except:
        conexaoDB.rollback()
        print("Erro!!! Unable to INSERT Data")

    cursor.close()
    conexaoDB.close()


def mostrarDados():
    conexaoDB = pymysql.connect(host="db4free.net", user="grupo8", password="12341234", database="proj_grupo8")
    cursor = conexaoDB.cursor()

    sql = 'SELECT * FROM minhaTabela'

    try:
        cursor.execute(sql)
        print(sql)
        results = cursor.fetchall()
        for row in results:
            valor = row[0]
            print("valores", valor)

    except:
        print("Erro!!! Unable to FETCH Data")

    cursor.close()
    conexaoDB.close()


def limpaTabela():
    conexaoDB = pymysql.connect(host="db4free.net", user="grupo8", password="12341234", database="proj_grupo8")
    cursor = conexaoDB.cursor()
    # sql = "DELETE from minhaTabela WHERE valores = 8"
    sql = "TRUNCATE TABLE minhaTabela"

    try:
        cursor.execute(sql)
        conexaoDB.commit()  # tornar mudanças permanentes no Banco de Dados

    except:
        conexaoDB.rollback()
        print("Erro!!! Unable to CLEAN Data")

    cursor.close()
    conexaoDB.close()


inserirDados(1)
mostrarDados()
"""

lista = calcula_bacterias(5)
print(lista)


def insereLista(lista):
    for i in range(0, len(lista)):
        # time.sleep(10)
        print(lista[i])
        inserirDados(lista[i])


def tamanhoLista(lista):
    return len(lista)


limpaTabela()
insereLista(lista)
"""