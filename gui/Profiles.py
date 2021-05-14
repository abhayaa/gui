import sys
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ShippingBox(QGroupBox):
	def __init__(self, title):
		super(QGroupBox, self).__init__(title)
		self.setTitle(title)

		self.first_name_tbox = QLineEdit()
		self.first_name_tbox.setPlaceholderText('First name')
		self.last_name_tbox = QLineEdit()
		self.last_name_tbox.setPlaceholderText('Last name')

		self.address1_tbox = QLineEdit()
		self.address1_tbox.setPlaceholderText('Address line 1')
		self.address2_tbox = QLineEdit()
		self.address2_tbox.setPlaceholderText('Address line 2')

		self.country_cbox = QComboBox()
		self.country_cbox.addItems(['Country', 'United States', 'Canada', 'Australia'])

		self.city_tbox = QLineEdit()
		self.city_tbox.setPlaceholderText('City')

		self.postal_tbox = QLineEdit()
		self.postal_tbox.setPlaceholderText('Postal code')

		self.state_cbox = QComboBox()
		self.state_cbox.addItems(['State','Alabama','Alaska','Arizona','Arkansas','California',
                                    'Colorado','Connecticut','Delaware','Florida',
                                    'Georgia','Hawaii','Idaho','Illinois','Indiana',
                                    'Iowa','Kansas','Kentucky','Louisiana','Maine',
                                    'Maryland','Massachusetts','Michigan','Minnesota',
                                    'Mississippi','Missouri','Montana','Nebraska','Nevada',
                                    'New Hampshire','New Jersey','New Mexico','New York',
                                    'North Carolina','North Dakota','Ohio','Oklahoma','Oregon',
                                    'Pennsylvania','Rhode Island','South Carolina','South Dakota',
                                    'Tennessee','Texas','Utah','Vermont','Virginia','Washington',
                                    'West Virginia','Wisconsin','Wyoming'])

		layout = QFormLayout()
		layout.addRow(self.first_name_tbox, self.last_name_tbox)
		layout.addRow(self.address1_tbox)
		layout.addRow(self.address2_tbox)
		layout.addRow(self.country_cbox)
		layout.addRow(self.city_tbox)
		layout.addRow(self.postal_tbox)
		layout.addRow(self.state_cbox)

		self.setLayout(layout)

class PaymentBox(QGroupBox):
	def __init__(self):
		super(QGroupBox, self).__init__()
		self.setTitle('Payment Details')

		self.first_name_tbox = QLineEdit()
		self.first_name_tbox.setPlaceholderText('First name')
		self.last_name_tbox = QLineEdit()
		self.last_name_tbox.setPlaceholderText('Last name')

		self.cardnum_tbox = QLineEdit()
		self.cardnum_tbox.setPlaceholderText('Card Number')

		hbox = QHBoxLayout()

		self.expirem_cbox = QComboBox()
		self.expirem_cbox.addItems(['MM','01','02','03','04','05','06','07','08','09','10','11','12'])

		self.button = QPushButton('Save', self)
		self.button.setToolTip('Save Profile')

		self.expirey_cbox = QComboBox()
		year = datetime.today().year-2000
		years = ['YY']
		years.extend([str(y) for y in range(year, year+11)])
		self.expirey_cbox.addItems(years)

		self.cvv_tbox = QLineEdit()
		self.cvv_tbox.setPlaceholderText('CVV Code')

		hbox.addWidget(self.expirem_cbox)
		hbox.addWidget(self.expirey_cbox)
		hbox.addWidget(self.cvv_tbox)

		layout = QFormLayout()
		layout.addRow(self.first_name_tbox, self.last_name_tbox)
		layout.addRow(self.cardnum_tbox)
		layout.addRow(hbox)
		layout.addRow(self.button)


		self.setLayout(layout)