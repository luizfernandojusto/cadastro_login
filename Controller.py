import hashlib


from Model import *
from Dao import *


class CadastroController:
    def cadastrar(self, cadastro: Cadastro):

        if len(cadastro.nome) >= 10 and len(cadastro.nome) <= 50:
            if "@" in cadastro.email and ".com" in cadastro.email:
                if len(cadastro.senha) > 8:
                    cadastro.senha = criptografar_senha(cadastro.senha)
                    c = CadastroDao.cadastrar(cadastro)
                    if c:
                        print("Cadastro realizado com sucesso!")
                    else:
                        print(
                            f"O email {cadastro.email} já existe! Cadastro não realizado."
                        )
                else:
                    print(f"Favor digitar senha válida!")
            else:
                print(f"Favor digitar e-mail válido!")
        else:
            print(
                f"O nome precisa ter mais de 10 caracteres. O que foi informado possui {len(cadastro.nome)} caracteres."
            )


def criptografar_senha(senha):

    sha256 = hashlib.sha256()
    sha256.update(senha.encode("utf-8"))
    senha_critografada = sha256.hexdigest()

    return senha_critografada


class LoginController:
    def acesso(self, cadastro: Cadastro):
        cadastro.senha = criptografar_senha(cadastro.senha)

        c = LoginDao.acesso(cadastro)
        if c:
            print(f"O usuario {c.nome} do email {c.email} acessou com sucesso!")
        else:
            print(f"E-mail ou senha invalido!")
