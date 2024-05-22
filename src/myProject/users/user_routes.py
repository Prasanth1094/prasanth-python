from flask import Blueprint,jsonify,request
from src.myProject.users.user_db import get_users,add_user
from src.myProject.database.db import connect

user_routes=Blueprint('user_routes', __name__)
@user_routes.route('/user', methods=['GET','POST'])
def get_user():   
       rows=get_users()
       data=[]    
       print(rows)
       for row in rows: 
          print(row,'insiode for loop')
          result={'id':row[0],'name':row[1],'email':row[2],'age':row[3]}     
          data.append(result)   
       return  jsonify(data)
@user_routes.route('/user/1', methods=['GET'])
def create_user():
     user=add_user()
     print (user)
     return 'Welcome to the login '
