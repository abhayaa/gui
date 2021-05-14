import sys
import json
import sqlite3

from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


con = sqlite3.connect('store.db')
cur = con.cursor()

# cur.execute('''CREATE TABLE accounts
#                 (account text, password text)''')

class AccountBox(QGroupBox):
    def __init__(self, title):

        super(QGroupBox, self).__init__(title)
        self.setTitle('Add Accounts')

        # self.store_cbox = QComboBox()
        # self.store_cbox.addItems(['Walmart', 'Target', 'BestBuy', 'Amazon'])

        self.username_tbox = QLineEdit()
        self.username_tbox.setPlaceholderText('Username/Email')
        self.password_tbox = QLineEdit()
        self.password_tbox.setEchoMode(QLineEdit.Password)

        layout = QGridLayout()
        # layout.addWidget(self.store_cbox, 0, 1)
        layout.addWidget(self.username_tbox,1, 1)
        layout.addWidget(self.password_tbox, 2, 1)

        self.button = QPushButton('Save', self)
        self.button.setToolTip('Save Profile')
        self.button.clicked.connect(self.on_save_click)
        layout.addWidget(self.button, 3, 1)

        layout.setColumnStretch(0,2)
        layout.setColumnStretch(1,2)
        layout.setColumnStretch(2,2)

        self.setLayout(layout)

    def on_save_click(self):
        #store = str(self.store_cbox.currentText())
        username = self.username_tbox.text()
        password = self.password_tbox.text()

        account_obj = {}
        #account_obj['store'] = store
        account_obj['username'] = username
        account_obj['password'] = password

        json_data = json.dumps(account_obj)
        with con:
            cur.execute('INSERT INTO accounts (account, password) values (?, ?)', (username, password))
        
        #just for testing 
        QMessageBox.question(self, 'Account JSON', json_data, QMessageBox.Yes| QMessageBox.No, QMessageBox.No)

class AccountsDisplayBox(QGroupBox):
    def __init__(self, Title):
        super(QGroupBox, self).__init__()
        self.setTitle('Accounts Added')

        self.button = QPushButton('Refresh', self)

        listdisplay = QListWidget()

        layout = QFormLayout()
        layout.addRow(listdisplay)
        layout.addRow(self.button)
        
        self.setLayout(layout)


        
