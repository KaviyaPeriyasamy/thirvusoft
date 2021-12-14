# Copyright (c) 2021, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSMeeting(Document):
	def validate(self):
		t=self.ts_to_time
		f=self.ts_from_time
		
		self.duration = 100
	