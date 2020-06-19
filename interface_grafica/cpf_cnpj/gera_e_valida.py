import sys
import geradores_validadores.cnpj as cnpj
import geradores_validadores.cpf as cpf
import interface_grafica.cpf_cnpj.design as design
from PyQt5.QtWidgets import QApplication, QMainWindow


class GeradorValidador(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_gera_cpf.clicked.connect(self.gera_cpf)
        self.btn_gera_cnpj.clicked.connect(self.gera_cnpj)
        self.btn_valida_cpf.clicked.connect(self.valida_cpf)
        self.btn_valida_cnpj.clicked.connect(self.valida_cnpj)

    def gera_cpf(self):
        cpf_gerado = cpf.gera_cpf()
        self.lbl_resultado_cpf.setText(cpf.formata(cpf_gerado))

    def gera_cnpj(self):
        cnpj_gerado = cnpj.gera_cnpj()
        self.lbl_resultado_cnpj.setText(cnpj.formata(cnpj_gerado))

    def valida_cpf(self):
        cpf_text = self.text_cpf.text()
        cpf_validado = cpf.valida_cpf(cpf_text)
        if cpf_validado:
            validado_text = f'{cpf.formata(cpf_text)} é válido'
        else:
            validado_text = f'{cpf.formata(cpf_text)} é inválido'
        self.lbl_resultado_cpf.setText(validado_text)

    def valida_cnpj(self):
        cnpj_text = self.text_cnpj.text()
        cnpj_validado = cnpj.valida_cnpj(cnpj_text)
        if cnpj_validado:
            validado_text = f'{cnpj.formata(cnpj_text)} é válido'
        else:
            validado_text = f'{cnpj.formata(cnpj_text)} é inválido'
        self.lbl_resultado_cnpj.setText(validado_text)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gerador_validador = GeradorValidador()
    gerador_validador.show()
    qt.exec_()
