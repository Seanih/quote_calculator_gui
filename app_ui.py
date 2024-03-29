# Form implementation generated from reading ui file '../qt_designer/contractor_app_ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(413, 284)
        self.formLayoutWidget = QtWidgets.QWidget(parent=Calculator)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 20, 244, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.input_form_layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.input_form_layout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_form_layout.setContentsMargins(0, 0, 0, 0)
        self.input_form_layout.setObjectName("input_form_layout")
        self.length_input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.length_input.setObjectName("length_input")
        self.input_form_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.length_input
        )
        self.width_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.width_label.setObjectName("width_label")
        self.input_form_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.width_label
        )
        self.width_input = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.width_input.setObjectName("width_input")
        self.input_form_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.width_input
        )
        self.apply_discount_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.apply_discount_label.setObjectName("apply_discount_label")
        self.input_form_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.apply_discount_label
        )
        self.discount_layout = QtWidgets.QHBoxLayout()
        self.discount_layout.setObjectName("discount_layout")
        self.no_radio = QtWidgets.QRadioButton(parent=self.formLayoutWidget)
        self.no_radio.setObjectName("no_radio")
        self.discount_layout.addWidget(self.no_radio)
        self.yes_radio = QtWidgets.QRadioButton(parent=self.formLayoutWidget)
        self.yes_radio.setObjectName("yes_radio")
        self.discount_layout.addWidget(self.yes_radio)
        self.input_form_layout.setLayout(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.discount_layout
        )
        self.length_label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.length_label.setObjectName("length_label")
        self.input_form_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.length_label
        )
        self.create_quote_btn = QtWidgets.QPushButton(parent=Calculator)
        self.create_quote_btn.setGeometry(QtCore.QRect(150, 130, 113, 32))
        self.create_quote_btn.setObjectName("create_quote_btn")
        self.formLayoutWidget_2 = QtWidgets.QWidget(parent=Calculator)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(120, 180, 171, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.output_form_layout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.output_form_layout.setLabelAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.output_form_layout.setFormAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.output_form_layout.setContentsMargins(0, 0, 0, 0)
        self.output_form_layout.setObjectName("output_form_layout")
        self.area_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.area_label.setAutoFillBackground(False)
        self.area_label.setObjectName("area_label")
        self.output_form_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.area_label
        )
        self.area_answer = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.area_answer.setObjectName("area_answer")
        self.output_form_layout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.area_answer
        )
        self.discount_amount_answer = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.discount_amount_answer.setObjectName("discount_amount_answer")
        self.output_form_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.discount_amount_answer
        )
        self.price_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.price_label.setObjectName("price_label")
        self.output_form_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.price_label
        )
        self.discount_amount_label = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.discount_amount_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.discount_amount_label.setObjectName("discount_amount_label")
        self.output_form_layout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.discount_amount_label
        )
        self.price_answer = QtWidgets.QLabel(parent=self.formLayoutWidget_2)
        self.price_answer.setObjectName("price_answer")
        self.output_form_layout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.price_answer
        )

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.width_label.setText(_translate("Calculator", "Floor Width:"))
        self.apply_discount_label.setText(
            _translate("Calculator", "Apply 15% Discount?:")
        )
        self.no_radio.setText(_translate("Calculator", "No"))
        self.yes_radio.setText(_translate("Calculator", "Yes"))
        self.length_label.setText(_translate("Calculator", "Floor Length:"))
        self.create_quote_btn.setText(_translate("Calculator", "Create Quote"))
        self.area_label.setText(_translate("Calculator", "Area Coverage:"))
        self.area_answer.setText(_translate("Calculator", "Area"))
        self.discount_amount_answer.setText(_translate("Calculator", "Discount"))
        self.price_label.setText(_translate("Calculator", "Total Price:"))
        self.discount_amount_label.setText(_translate("Calculator", "Discount:"))
        self.price_answer.setText(_translate("Calculator", "Price"))
