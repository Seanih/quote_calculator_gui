import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QFormLayout,
    QComboBox,
    QTextEdit,
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QMenuBar,
    QToolBar,
    QMenu,
    QListWidget,
    QListWidgetItem,
    QTableWidget,
    QTableWidgetItem,
    QDockWidget,
    QSpinBox,
    QMessageBox,
)
from PyQt6.QtGui import QAction, QTextCursor, QColor, QIcon  # menu bar actions
from PyQt6.QtCore import Qt, QSize

# import ui
from app_ui import Ui_Calculator


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 500)

        # create UI object and call setup function
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.setWindowTitle("Contract Calculator")

        # access objects like normal
        self.ui.no_radio.setChecked(True)
        self.ui.area_answer.setText("0")
        self.ui.discount_amount_answer.setText("N/A")
        self.ui.price_answer.setText("0")

        self.ui.create_quote_btn.clicked.connect(self.calculate_area)

    def calculate_area(self):
        # reset discount if previous calculation was made
        self.ui.discount_amount_answer.setText("N/A")

        if self.ui.length_input.text() and self.ui.width_input.text():
            length = self.ui.length_input.text()
            width = self.ui.width_input.text()
            yes_discount = self.ui.yes_radio.isChecked()

            if (length.isdigit() or isinstance(float(length), float)) and (
                width.isdigit() or isinstance(float(width), float)
            ):
                # update square footage
                self.ui.area_answer.setText(f"{(float(length) * float(width)):.1f} ft²")

                price = float(20 * (float(length) * float(width)))

                if yes_discount:
                    discount_amount = 0.15 * price
                    discounted_price = price - discount_amount

                    self.ui.discount_amount_answer.setText(f"${discount_amount:.2f}")
                    self.ui.price_answer.setText(f"${discounted_price:.2f}")

                else:
                    # update total price
                    self.ui.price_answer.setText(f"${price:.2f}")

            else:
                print("at least one isn't a number...")
        else:
            print("Can't leave blank spaces")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
