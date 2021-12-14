# Copyright (c) 2021, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TSMeeting(Document):
	def validate(self):
		t=self.ts_to_time
		f=self.ts_from_time
		th=int(t[0:2])
		tm=int(t[3:5])
		ts=int(t[6:8])
		fh=int(f[0:2])
		fm=int(f[3:5])
		fs=int(f[6:8])
		dh=th-fh
		dm=tm-fm
		ds=ts-fs
		d=""
		d=d+str(dh)
		d=d+":"+str(dm)
		d=d+":"+str(ds)

		self.ts_duration = d
	