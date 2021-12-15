# Copyright (c) 2021, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSMember(Document):
	def validate(self):
		if(self.ts_corl=="Client Meet"):
			if(self.ts_cphone.isdigit() and len(self.ts_cphone)==10 and int(self.ts_cphone[0]) in range(6,10)):
				{}
			else:
				{
				frappe.throw("Please enter valide phone number in client contact number")
				}
			if(self.ts_cpcn.isdigit() and len(self.ts_cpcn)==10 and int(self.ts_cpcn[0]) in range(6,10)):
				{}
			else:
				{
				frappe.throw("Please enter valide phone number in Participant contact number")
				}
		else:
			if(self.ts_mlcn.isdigit() and len(self.ts_mlcn)==10 and int(self.ts_mlcn[0]) in range(6,10)):
				{}
			else:
				{
				frappe.throw("Please enter valide phone number in Meet lead Contact Number")
				}
			if(self.ts_pcn.isdigit() and len(self.ts_pcn)==10 and int(self.ts_pcn[0]) in range(6,10)):
				{}
			else:
				{	
					frappe.throw("Please enter valide phone number in Participant Contact Number")
				}
