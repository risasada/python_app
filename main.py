import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

from function import function


class ExampleWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 190)
        self.move(300, 300)
        self.setWindowTitle('Aipatch')

        # buttonの設定
        self.button = QPushButton('attach')

        # buttonのclickでラベルをクリア
        self.button.clicked.connect(lambda: function())
        self.button.clicked.connect(self.button_clicked)

        # レイアウト配置
        self.grid = QGridLayout()
        self.grid.addWidget(self.button, 0, 0, 1, 1)
        self.setLayout(self.grid)

        # 表示
        self.show()


    def button_clicked(self):
        if self.button.isChecked():
            self.button.setEnabled(False)
            self.button.setText('In operation')
        else:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ew = ExampleWidget()
    sys.exit(app.exec_())
