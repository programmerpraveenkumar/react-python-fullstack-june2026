""" -> doc string
http methods
get post ,put ,delete
in server programming all methods should return
to run the app:
    uvicorn main:app
"""

# importing the fastapi from fastapi modules 
from fastapi import FastAPI
from model.data import Register,Login

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


# www.google.com->show search screen
#www.google.com/enddpoint1/enddpoint2/enddpoint3?
#www.google.com/gmail->gmail screen
#www.google.com/youtube->youtube screen
#www.chatgpt.com->show the search screen