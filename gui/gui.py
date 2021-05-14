import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Profiles import *
from Accounts import *



def main():
    app = QApplication(sys.argv)

    w = QTabWidget()
    w.resize(800, 500)
    w.setWindowTitle('COBOT V. 0.0')

    w.addTab(ProfilesTab(), 'Profiles')
    w.addTab(AccountsTab(), 'Accounts')


    w.show()
    sys.exit(app.exec_())

class ProfilesTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        hbox = QHBoxLayout()

        shipping_gbox = ShippingBox('Shipping')
        billing_gbox = ShippingBox('Billing Info')
        payment_gbox = PaymentBox()
        hbox.addWidget(shipping_gbox)
        hbox.addWidget(billing_gbox)
        hbox.addWidget(payment_gbox)

        self.setLayout(hbox)


class AccountsTab(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        hbox = QHBoxLayout()

        acounts_gbox = AccountBox("Accounts")
        account_display = AccountsDisplayBox("Accounts")
        hbox.addWidget(acounts_gbox)
        hbox.addWidget(account_display)

        self.setLayout(hbox)

# class DashboardTab(QWidget):
#     def __init__(self):
#         super(QWidget, self).__init__()
      




# class SettingsTab(QWidget):
#     def __init__(self):
#         super(QWidget, self).__init__()



if __name__ == '__main__':
    main()
