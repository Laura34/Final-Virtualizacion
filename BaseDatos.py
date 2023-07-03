from mysql.connector import Error
from mysql.connector import connect


class Conexion:
    def __init__(self):
        self.database = 'Final'

    def conectar(self, user, password, host):
        self.user=user
        self.password=password
        self.host=host
        try:
            self.connection = connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                return '¡Conexión Exitosa!'
        except Error as e:
            return ('Error' +'\n'+  str(e))


    def leerUsuarios(self):
        self.conectar(self.user, self.password, self.host)
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            try:
                self.cursor.execute("""SELECT * FROM usuarios;""")
            except Error as e:
                return "¡Error!" + '\n' + str(e)
            estudiantes = self.cursor.fetchall()
            self.connection.close()
            return estudiantes

    def leerPeliculas(self):
        self.conectar(self.user, self.password, self.host)
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            try:
                self.cursor.execute("""SELECT * FROM peliculas;""")
            except Error as e:
                return "¡Error!" + '\n' + str(e)
            estudiantes = self.cursor.fetchall()
            self.connection.close()
            return estudiantes