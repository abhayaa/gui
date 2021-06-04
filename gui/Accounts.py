import sys
import json
import sqlite3

from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.script import *

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
        

class AccountsDisplayBox(QGroupBox):
    def __init__(self, Title, displaybox):
        super(QGroupBox, self).__init__()
        self.setTitle('Accounts Added')
        
        listdisplay = QListWidget()
        self.displaybox = listdisplay
        
        with con: 
            cur.execute('SELECT account FROM accounts;')
            accounts = cur.fetchall()


        for account in accounts:
            item = QListWidgetItem(account[0])
            listdisplay.addItem(item)

        layout = QFormLayout()
        layout.addRow(listdisplay)

        self.startButton = QPushButton('Start', self)
        self.rbutton = QPushButton('Refresh', self)
        self.dbutton = QPushButton('Delete', self)
        self.rbutton.setToolTip('Refresh Accounts')
        self.dbutton.setToolTip('Delete Account')
        self.rbutton.clicked.connect(self.on_refresh_click)
        self.dbutton.clicked.connect(self.on_delete_click)
        self.startButton.clicked.connect(self.on_start_click)
        layout.addRow(self.rbutton)
        layout.addRow(self.dbutton)
        layout.addRow(self.startButton)
        
        self.setLayout(layout)

    def on_refresh_click(self):
        
        accounts = []
        listdisplay = self.displaybox

        listdisplay.clear()

        with con: 
            cur.execute('SELECT account FROM accounts;')
            accounts = cur.fetchall()

        for account in accounts:
            item = QListWidgetItem(account[0])
            listdisplay.addItem(item)

    def on_delete_click(self):
        items = self.displaybox.selectedItems()
        for item in items:
            self.displaybox.takeItem(self.displaybox.row(item))
            with con:
                cur.execute("DELETE FROM accounts where account = ?", (item.text(),))

    def on_start_click(self):
        run_checkout()

