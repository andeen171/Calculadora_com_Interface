from UiCalculadora import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets # PyQt5 Nescessario pra rodar


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        global lista
        lista = [] # lista nescessaria para montar a expressao
        class status: status = True

        def calc(arg): # Check dos botões Ce e Off
            if arg == 'Off':
                self.visor.display('')
                lista.clear()
            elif arg == 'On/CE':
                self.visor.display('0')
                lista.clear()

            elif arg in '1234567890.': # Quando precionar um numero
                valor = str(self.visor.intValue())
                if len(lista) and lista[-1] == '.':
                    valor += '.'
                if str(self.visor.display(valor + arg)) != '0' and status.status == True:
                    self.visor.display(valor + arg)
                else:
                    self.visor.display(str(arg))
                lista.append(arg)
                status.status = True
            elif arg in '+-*/' and (all(map(lambda x: lista.count(x) <= 1, ['+', '-', '*', '/'])) and len(lista) and '+-'): # quando for um operador
                status.status = False
                if len(lista) and '+-*/' in lista[-1]:
                    del lista[-1]
                lista.append(arg)
            else: # do contrario tenta exibir o resultado
                if len(lista):
                    print(lista) # exibe a lista na janela do console para averiguação
                    status.status = False
                    self.visor.display(str(eval(''.join(lista).strip('+-*/=')))) # exibe o resultado da expressao feito com eval()
                    lista.clear() 
                    resultado = str(self.visor.value())
                    if resultado.endswith('.0'):
                        resultado = resultado.rsplit('.0', 1)[0]
                    lista.append(resultado)
                    if arg != '=': # se a ultima operação não for "=" o resultado e colocado na lista para proximos calculos
                        lista.append(arg)

        self.botao0_2.clicked.connect(lambda: calc(self.botao0_2.text()))
        self.botao00_2.clicked.connect(lambda: calc(self.botao00_2.text()))
        self.botao1_2.clicked.connect(lambda: calc(self.botao1_2.text()))
        self.botao2_2.clicked.connect(lambda: calc(self.botao2_2.text()))
        self.botao3_2.clicked.connect(lambda: calc(self.botao3_2.text()))
        self.botao4_2.clicked.connect(lambda: calc(self.botao4_2.text()))
        self.botao5_2.clicked.connect(lambda: calc(self.botao5_2.text()))
        self.botao6_2.clicked.connect(lambda: calc(self.botao6_2.text()))
        self.botao7_2.clicked.connect(lambda: calc(self.botao7_2.text()))
        self.botao8_2.clicked.connect(lambda: calc(self.botao8_2.text()))
        self.botao9_2.clicked.connect(lambda: calc(self.botao9_2.text()))
        self.botaoponto_2.clicked.connect(lambda: calc(self.botaoponto_2.text()))
        self.botaomais_2.clicked.connect(lambda: calc(self.botaomais_2.text()))
        self.botaodiv_2.clicked.connect(lambda: calc(self.botaodiv_2.text()))
        self.botaomult_2.clicked.connect(lambda: calc(self.botaomult_2.text()))
        self.botaomenos_2.clicked.connect(lambda: calc(self.botaomenos_2.text()))
        self.botaoresult.clicked.connect(lambda: calc(self.botaoresult.text()))
        self.pushButton.clicked.connect(lambda: calc(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: calc(self.pushButton_2.text()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
