# Copyright (c) 2021, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSPayroll(Document):
	def validate(self):
		if(len(self.ts_phone) != 10 or int(self.ts_phone[0]) not in range(6,10)):
			frappe.throw("Invalid Phone Number")
		else:
			self.ts_phone=self.ts_phone
		
		d={"Software Developer":8100,"Designer":8000,"Marketing":10000,"Tech lead":30000,"House Keeping":11000}
		self.ts_basic=d[self.ts_role]
		#if(int(self.ts_from[-1:-2])==int(self.ts_to[-1:-2]) or int(self.ts_from[-4:-5])!=int(self.ts_to[-4:-5]) ):
			#frappe.throw("Enter valid date")