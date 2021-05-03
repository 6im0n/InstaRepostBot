# InstaRepostBot 📈
Script to repost content based on hashtag or a account to your profile, with mention of owner and tag of him
inspired by this repo : https://github.com/Duckcouncil/instagramThief

I can be responsable of instagram change... 
last time tested: 
02/05/2021 python 3.9

<h2>Before start</h2>
change the line 59 and place your tag here

'''self.driver.get("https://www.instagram.com/explore/tags/PLACEYOURTAG/")'''
example : for the #github tag

'''self.driver.get("https://www.instagram.com/explore/tags/github/")'''

AND add you custom parameter here config.py
how to create database and a user in postgresql
'''su postgresql'''
'''psql'''
'''psql=#CREATE USER youruser WITH PASSWORD 'yourpass';
'''psql=#createdb dbname;''
'''psql=# grant all privileges on database <dbname> to <username> ;'''
and launch createDataBase.py to create table and constraints (not forget to add your password, user, and database name to your config.py)
database used for this purpose : postgreSQL 

things to do :
+ Make a system to select time interval
+ Make a UI 
+ more details for the readMe
