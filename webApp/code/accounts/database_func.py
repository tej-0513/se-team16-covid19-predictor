from pymongo import MongoClient, errors
Domain='127.0.0.1'
port=27017

class mongo_DB:

	def __init__(self):
		self.connection=MongoClient("mongodb://apurvi:1234@127.0.0.1/db2")
		self.db=self.connection.db2

	def insert(self,cl_name,db_entry):
		# self.db.cl_name.insert_one(db_entry)

		if cl_name=="patient_details":
			self.db.patient_details.insert_one(db_entry)

		elif cl_name=="equipment_details":
			self.db.equipment_details.insert_one(db_entry)

		elif cl_name=="request_details":
			self.db.request_details.insert_one(db_entry)

		elif cl_name=="output_details":
			self.db.output_details.insert_one(db_entry)

		else:
			return False 


	def check_perDayEntry(self,cl_name,check_entry): # for check entry enter hospit_name zone and date 
		
		if cl_name=="patient_details":
			
			return (self.db.patient_details.count_documents(check_entry)==1)
			
		if cl_name=="equipment_details":
			
			return (self.db.equipment_details.count_documents(check_entry)==1)
		


	def update(self,cl_name,entry_type,updated_entry):

		if cl_name=="zone_data" and entry_type=='patient_update':
			#received values
			
			zone=updated_entry['zone']
			

			#find old values
			db_values=self.db.zone_data.find({'zone':zone})
			
			for x in db_values:
				new_active=x['active']+updated_entry['active']
				new_recovered=x['recovered']+updated_entry['recovered']
				new_death=x['death']+updated_entry['death']

			print("new active \n",new_active)
			#update
			self.db.zone_data.update_one({"zone":zone},{"$set":{"active":new_active,"recovered":new_recovered,"death":new_death}})

		elif cl_name=="zone_data" and entry_type=='equipment_update':
			#received values
			
			zone=updated_entry['zone']
			

			#find old values
			db_values=self.db.zone_data.find({'zone':zone})
			for x1 in db_values:
				new_beds=x1['empty_beds']+updated_entry['empty_beds']
				new_ven=x1['empty_ven']+updated_entry['empty_ven']
				new_ppe=x1['ppe_stock']+updated_entry['ppe_stock']

			#update
			self.db.zone_data.update_one({"zone":zone},{"$set":{"empty_beds":new_beds,"empty_ven":new_ven,"ppe_stock":new_ppe}})

		else:
			return False


	def entire_collection(self,cl_name): # returns cursor object
		if cl_name=="patient_details":
			return self.db.patient_details.find()

		elif cl_name=="equipment_details":
			return self.db.equipment_details.find()

		elif cl_name=="request_details":
			return self.db.request_details.find()

		elif cl_name=="output_details":
			return self.db.output_details.find()

		elif cl_name=="zone_data":
			return self.db.zone_data.find()

		else:
			return False 
		
	def drop_collection(self,cl_name):
		
		if cl_name=='output_details':
			self.db.output_details.drop()

		elif cl_name=="zone_data":
			self.db.zone_data.drop()
			zone_list=['z1','z2','z3','z4']

			for z in zone_list:
				db_entry={'zone':z,'active':0,'recovered':0,'death':0,'empty_beds':0,'empty_ven':0,'ppe_stock':0}
				self.db.zone_data.insert_one(db_entry)

		else:
			return False

	def delete(self,cl_name,db_entry):
		if cl_name=="patient_details":
			return self.db.patient_details.delete_many(db_entry)


		elif cl_name=="equipment_details":
			return self.db.equipment_details.delete_many(db_entry)


		elif cl_name=="request_details":
			return self.db.request_details.delete_many(db_entry)


		elif cl_name=="output_details":
			return self.db.output_details.delete_many(db_entry)


		elif cl_name=="zone_data":
			return self.db.zone_data.delete_many(db_entry)

		else:
			return False 
		


# def main():
# 	mdb=mongo_DB()
# 	#------------------- Check1 : Enter Patient Details----------------------------------
# 	check=mdb.check_perDayEntry("patient_details",{'name':'jyoti','zone':'z1','date':'1/2/19'})
# 	if(check==True):
# 		print("Duplicate Entry")

# 	else:

# 		print("Making entry")

# 		val=mdb.insert("patient_details",{'name':'jyoti','zone':'z1','date':'1/2/19','active':2,'recovered':3,'death':1})
# 		mdb.update('zone_data','patient_update',{'zone':'z1','active':1,'recovered':3,'death':1})
# 		table_entries=mdb.entire_collection('zone_data')
# 		print('done')


# 	#------------------------Check2 : Enter Equipment details-------------------------------------
# 	check=mdb.check_perDayEntry("equipment_details",{'name':'jyoti','zone':'z1','date':'1/2/19','empty_beds':10,'empty_ven':5,'ppe_stock':1})
# 	if(check==True):
# 		print("Duplicate Entry")

# 	else:

# 		print("Making entry")
# 		val=mdb.insert("equipment_details",{'name':'jyoti','zone':'z1','date':'1/2/19','empty_beds':10,'empty_ven':5,'ppe_stock':1})
# 		mdb.update('zone_data','equipment_update',{'zone':'z1','empty_beds':10,'empty_ven':5,'ppe_stock':1})
# 		print('done')

# 	#----------------------Check3 insert other  table-----------------------------------
# 	val=mdb.insert("request_details",{'name':'jyoti','zone':'z1','date':'1/2/19','empty_beds':10,'empty_ven':5,'ppe_stock':1})
# 	val=mdb.insert("request_details",{'name':'jyoti','zone':'z2','date':'1/2/19','empty_beds':10,'empty_ven':5,'ppe_stock':1})

# 	val=mdb.insert("output_details",{'name':'jyoti','zone':'zi','date':'1/2/19','empty_beds':10,'empty_ven':5,'ppe_stock':1})
		
# 	#-------------------------Cursor Object return-------------------------------------
# 	table_entries=mdb.entire_collection('output_details')
# 	table_entries=mdb.entire_collection('zone_data')
# 	# print('type ',type(table_entries))
# 	for x in table_entries:
# 		print('table entry : ',x['zone'])

# 	#------------------Request Delete--------------------------------------------------
# 	mdb.delete("request_details",{'name':'jyoti','zone':'z2','date':'1/2/19'})

# 	#----------------------------Drop collection--------------------------------------------
# 	# mdb.drop_collection('output_details')
# 	# mdb.drop_collection('zone_data')

# if __name__=='__main__':
# 	main()