from passlib.hash import pbkdf2_sha256 as crypt

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome =  sobrenome
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=1000, salt_size=10)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        return crypt.verify(senha, self.__senha)

while True:
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    confirma_senha = input("Confirme a senha: ")
    if senha == confirma_senha:
        break
    else:
        print("Senhas não conferem!")

user = Usuario(nome, sobrenome, email, senha)
print("Usuário Criado com Sucesso!")

print("Login....")
senha = input("Digite a senha de acesso: ")

if user.checa_senha(senha):
    print("Acesso permitido! ")
else:
    print("Acesso Negado! ")