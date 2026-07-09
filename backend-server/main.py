""" -> doc string
http methods
get post ,put ,delete
in server programming all methods should return
to run the app:
    uvicorn main:app
"""

# importing the fastapi from fastapi modules 
from fastapi import FastAPI
from model.data import Register,Login,AddCart
from db_connection import getConnection
app = FastAPI()



@app.get("/")
def sample_get():
    """
        this mehtod will return the string
    """
    return "hello world"

@app.get("/gmail")
def sample_get(name:str):
    """
        we can recv upto 1000 to 2000chars
        this mehtod will return the string
    """
    return "person name is "+name


@app.get("/climate")
def climate_method(type:str,total:int):
    if type == "rain":
        if total >5:
            return "heavy rain fall"
        else:
            return " just rain.."
    elif type == "summer":
        if total > 40:
            return "very hot!!"
        else:
            return "its cool"
    else:
        return "type is not found"
    

@app.post('/user-register')
def user_register(register_obj:Register):
    return register_obj.name+" "+str(register_obj.mobile)


@app.post('/add-cart')
def add_cart(cart_obj:AddCart):
    return cart_obj.name+" "+str(cart_obj.qty)



@app.get("/user")
def get_all_user():
    """
      get all users from database
    """
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from user1")
    allrows = cursor.fetchall()
     # close the connection if no need of db connection
    cursor.close()
    connection.close()
    return allrows

@app.post("/user")
def post_user(register_obj:Register):
# db query steps
# connection open,cursor open,execution,cur.close,conn.close()
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"insert into user1(name, email, mobile, password, dob)values('{register_obj.name}','{register_obj.email}','{register_obj.mobile}','{register_obj.password}','{register_obj.dob}')")
        # to commit the actions
        connection.commit()
        cursor.close()
        connection.close()
        return "data inserted"
    except Exception as e:
        # convert error to string
        return str(e)

# www.google.com->show search screen
#www.google.com/enddpoint1/enddpoint2/enddpoint3?
#www.google.com/gmail->gmail screen
#www.google.com/youtube->youtube screen
#www.chatgpt.com->show the search screen