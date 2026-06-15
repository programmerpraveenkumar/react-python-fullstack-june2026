#class declaration
class Login:
    # email declaration
    def check_email(email_txt):
        if "@gmail.com" in email_txt:
            print("yes this is email")
        else:
            print("yes this is not email")

#object created for login class
login_obj = Login()
login_obj.check_email("asdfasdfds")
login_obj.check_email("asdf@gmail.com")
