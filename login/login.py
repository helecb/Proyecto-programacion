import os
from kivymd.app import MDApp
from clases.usuario import Usuario
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_file(os.path.join(os.path.dirname(__file__), "login.kv"))

class LoginScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"

    # Se ejecuta cuando en el .kv se escribe root.registrar()
    def iniciar(self):
        app= MDApp.get_running_app()

        correo = self.ids.correo.text.strip()
        contrasena = self.ids.contrasena.text

        if correo == "" or contrasena == "":
            print("Error: completá todos los campos")
            return

        usuario_encontrado = None

        for usuario in app.usuarios:
            if usuario.correo == correo:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            print("Error: no existe un usuario con ese correo")
            return

        if not usuario_encontrado.contrasena_correcta(contrasena):
            print("Error: contraseña incorrecta")
            return

        app.usuario_actual = usuario_encontrado
        print("Inicio de sesión válido")

        self.manager.current = "home"


