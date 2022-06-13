from flask import Flask,render_template,request
import getpass
import sys
import telnetlib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("app.js")

@app.route("/router1_name", methods=['GET'])
def router1_name():

            # output = request.form.to_dict()
            # print(output)
            # name = output["name"]
    
            # HOST = "192.168.56.10"
            # user = input("Enter votre tlnet username:")
            # password = getpass.getpass()

            # tn = telnetlib.Telnet(HOST)

            # tn.read_until(b"Username")
            # tn.write(user.encode("ascii") + b"\n")
            # if password:
            #     tn.read_until(b"Password", timeout=None)
            #     tn.write(password.encode("ascii") + b"\n")


            # tn.write(b"enable\n")
            # tn.write(b"conf t\n")
            # tn.write(b"hostname {}\n".format(name))
            # tn.write(b"exit\n")

            # print(tn.read_all())

            args = request.args

            return {"result": args.get("name")}

@app.route("/router1_config")
def router1_config():

            # output = request.form.to_dict()
            # print(output)
            # name = output["name"]
    
            # HOST = "192.168.56.10"
            # user = input("Enter votre tlnet username:")
            # password = getpass.getpass()

            # tn = telnetlib.Telnet(HOST)

            # tn.read_until(b"Username")
            # tn.write(user.encode("ascii") + b"\n")
            # if password:
            #     tn.read_until(b"Password", timeout=None)
            #     tn.write(password.encode("ascii") + b"\n")


            # tn.write(b"enable\n")
            # tn.write(b"conf t\n")
            # tn.write(b"hostname {}\n".format(name))
            # tn.write(b"exit\n")

            # print(tn.read_all())

            return {"result": "ROUTER1 is Configured"} 

@app.route("/router1_clear")
def router1_clear():

            # output = request.form.to_dict()
            # print(output)
            # name = output["name"]
    
            # HOST = "192.168.56.10"
            # user = input("Enter votre tlnet username:")
            # password = getpass.getpass()

            # tn = telnetlib.Telnet(HOST)

            # tn.read_until(b"Username")
            # tn.write(user.encode("ascii") + b"\n")
            # if password:
            #     tn.read_until(b"Password", timeout=None)
            #     tn.write(password.encode("ascii") + b"\n")


            # tn.write(b"enable\n")
            # tn.write(b"conf t\n")
            # tn.write(b"hostname {}\n".format(name))
            # tn.write(b"exit\n")

            # print(tn.read_all())

            return {"result": "ROUTER1 RIP Configuration is Cleared"}               



@app.route("/router2_name", methods=['GET'])
def router2_name():

            # output = request.form.to_dict()
            # print(output)
            # name = output["name"]
    
            # HOST = "192.168.43.47"
            # user = "zaki"
            # password = "123"

            # tn = telnetlib.Telnet(HOST)

            # #tn.read_until(b"Username")
            # tn.write(user.encode("ascii") + b"\n")
            # #if password:
            #     #tn.read_until(b"Password", timeout=None)
            # tn.write(password.encode("ascii") + b"\n")

            # #configuration commands
            # tn.write(b"enable\n")
            # tn.write(b"conf t\n")
            # tn.write(b"hostname {}\n".format(name))
            # tn.write(b"exit\n")

            # print(tn.read_all())

            args = request.args

            return {"result": args.get("name")}

@app.route("/router2_config")
def router2_config():

    
            # HOST = "localhost"
            # user = "zaki"
            # password = "123"
            # tn = telnetlib.Telnet(HOST)

            # #tn.read_until(b"Username")
            # tn.write(user.encode("ascii") + b"\n")
            # #if password:
            #     #tn.read_until(b"Password", timeout=None)
            # tn.write(password.encode("ascii") + b"\n")


            # tn.write(b"enable\n")
            # tn.write(b"conf t\n")
            # tn.write(b"hostname {}\n".format(name))
            # tn.write(b"exit\n")

            # print(tn.read_all())

            return {"result": "ROUTER2 is Configured"} 

@app.route("/router2_clear")
def router2_clear():

            # output = request.form.to_dict()
            # print(output)
            # name = output["name"]
    
            # HOST = "192.168.56.10"
            # user = input("Enter votre tlnet username:")
            # password = getpass.getpass()

            # tn = telnetlib.Telnet(HOST)

            # tn.read_until(b"Username")
            # tn.write(user.encode("ascii") + b"\n")
            # if password:
            #     tn.read_until(b"Password", timeout=None)
            #     tn.write(password.encode("ascii") + b"\n")


            # tn.write(b"enable\n")
            # tn.write(b"conf t\n")
            # tn.write(b"hostname {}\n".format(name))
            # tn.write(b"exit\n")

            # print(tn.read_all())

            return {"result": "ROUTER2 RIP Configuration is Cleared"}                                   

    
        


if __name__ == "__main__":
    app.run(debug=True, port = 8080)