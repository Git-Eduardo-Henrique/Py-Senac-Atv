import mysql.connector as ms


class DataVerificar:
    def __init__(self):
        # conecta com o banco de dados
        self.conectar = ms.connect(host='localhost', user='root', password='q1w2e3', database='Banco_Pack_Py')
        self.cursor = self.conectar.cursor()
        self.func = ''
        self.cli = ''

    def Cadastrar(self, cpf, nome, data, genero, email, senha, saldo):
        # realiza o cadastro no banco de dados
        self.cursor.execute(f'INSERT INTO cliente (cpf, nome, dataNasc, genero, email, senha, saldo) VALUES'
                            f'("{cpf}","{nome}","{data}","{genero}","{email}","{senha}","{saldo}")')

        self.conectar.commit()

    def Check_func(self, entry_id, entry_senha):
        self.cursor.execute(f'SELECT * FROM func')
        self.func = self.cursor.fetchall()
        for funcionario in self.func:
            if entry_id == funcionario[0] and entry_senha == funcionario[1]:
                return True
            else:
                return False

    def Check_cli(self, entry_cpf, entry_senha):
        self.cursor.execute('SELECT * FROM cliente')
        self.cli = self.cursor.fetchall()
        verifica = False
        for cliente in self.cli:
            if entry_cpf == cliente[0] and entry_senha == cliente[5]:
                verifica = True
            else:
                pass
        if verifica:
            return True
        else:
            return False

    def Close(self):
        self.cursor.close()
        self.conectar.close()


class Conta:
    def __init__(self):
        self.conectar = ms.connect(host='localhost', user='root', password='q1w2e3', database='Banco_Pack_Py')
        self.cursor = self.conectar.cursor()
        self.saq = ''

    def info_user(self, cpf):  # cria uma lista com as principais informações
        self.cursor.execute(f'select cpf, nome, saldo from cliente where cpf = "{cpf}";')
        infos = self.cursor.fetchall()
        lista = []
        for info in infos:
            lista.append(info[0])
            lista.append(info[1])
            lista.append(info[2])
        return lista

    def deposito(self, cpf, saldo):
        self.cursor.execute(f'UPDATE cliente SET saldo = saldo + {float(saldo)} WHERE cpf = "{cpf}" ')
        self.conectar.commit()

    def saque(self, cpf, saldo):
        self.cursor.execute(f'UPDATE cliente SET saldo = saldo - {float(saldo)} WHERE cpf = "{cpf}" ')
        self.conectar.commit()

    def verifica(self, cpf, saque):
        self.cursor.execute(f'SELECT saldo FROM cliente WHERE cpf = "{cpf}" ')
        self.saq = self.cursor.fetchall()
        verifica = False
        for dindin in self.saq:
            if float(dindin[0]) < float(saque):
                verifica = True
        if verifica:
            return False
        else:
            return True

    def Close(self):
        self.cursor.close()
        self.conectar.close()
