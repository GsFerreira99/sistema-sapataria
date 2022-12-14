from sistema.model.login_model import LoginModel
from sistema.view.login_view import LoginView


class LoginController:

    def __init__(self, db, parent=None):
        self.__db = db
        self.view = LoginView(parent)
        self.model = LoginModel(self.__db)

        self.view.btn_acessar.setAutoDefault(True)

    def acessar_sistema(self):
        self.model.definir_credenciais(self.view.receber_credenciais_login())
        autenticacao = self.model.autenticar()
        if autenticacao is not False:
            self.view.mensagem_erro(True)
            return autenticacao
        else:
            self.view.mensagem_erro(False)
