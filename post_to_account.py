import os
from instabot import Bot 
import psycopg2
import time
import io
import shutil
import string
from config import *

def postToAccount():
	print("starting....")
	db = psycopg2.connect(database=databaseName,user=db_user,password=passwordDataBase,host="127.0.0.1",port="5432")
	cursor = db.cursor()
	#bot = Bot() 
	os.chdir(Picture_path)
	#bot.login(username = username,  
	#		password = password)
	print("LOGIN SUCCESS !")
	r = cursor.execute("SELECT * FROM photos_instagram")
	rows = cursor.fetchall()
	for row in rows:
		owner = row[3]
		path = row[1]
		status = row[2]
		ID = row[0]
		caption = "Owner: " + "@"+ owner + "\n" + "————————— \n If you are the owner of the post and want to remove it, please contact me and I will remove it\n—————————\n TAG: \n—————————"
		print(caption);
		print("")
		print(status)
		print("")
		if str(status) != "POSTED":
			#bot.upload_photo(path,caption=caption)
			time.sleep(0)
			#Make change status on DB
			#sql_update_query = """Update photos_instagram set status = %s where id = %s"""
			#cursor.execute(sql_update_query% ("'POSTED'", "'"+ID+"'"))
			#db.commit()
			count = cursor.rowcount
			print(count, "Record Updated successfully ")
			#cursor.execute("SELECT * FROM photos_instagram WHERE id = "+"'"+ID+"'"+";")
			cursor.execute("UPDATE photos_instagram SET status = 'POSTED';")
			os.rename(ID+".jpeg.REMOVE_ME",ID+".jpeg")
			shutil.rmtree("HERE THE CONFIG FOLDER CREATE BY INSTABOTAPI")
			print("POSTED")
		else:
			pass
			print("NOTPOSTED")

	db.commit()
	db.close()
	
	print("PostgreSQL connection is closed")
postToAccount()
