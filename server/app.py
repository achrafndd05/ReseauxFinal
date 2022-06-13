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

    args = request.args

    HOST = "192.168.56.10"
    user = "user"
    password = "pass"

    tn = telnetlib.Telnet(HOST)

    tn.write(user.encode("ascii") + b"\n")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"hostname {}\n".format(args.get("name")))
    tn.write(b"exit\n")

    print(tn.read_all())


    return {"result": args.get("name")}

@app.route("/router1_config")
def router1_config():

    HOST = "192.168.56.10"
    user = "user"
    password = "pass"

    tn = telnetlib.Telnet(HOST)

    tn.write(user.encode("ascii") + b"\n")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"router rip\n")
    tn.write(b"network 10.0.0.0\n")
    tn.write(b"network 10.0.1.0\n")

    tn.write(b"exit\n")

    print(tn.read_all())

    return {"result": "ROUTER1 is Configured"} 

@app.route("/router1_clear")
def router1_clear():

    HOST = "192.168.56.10"
    user = "user"
    password = "pass"

    tn = telnetlib.Telnet(HOST)

    tn.write(user.encode("ascii") + b"\n")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"no router rip\n")

    tn.write(b"exit\n")

    print(tn.read_all())

    return {"result": "ROUTER1 RIP Configuration is Cleared"}               



@app.route("/router2_name", methods=['GET'])
def router2_name():

            args = request.args

            HOST = "192.168.56.20"
            user = "user"
            password = "pass"

            tn = telnetlib.Telnet(HOST)

            tn.write(user.encode("ascii") + b"\n")
            tn.write(password.encode("ascii") + b"\n")

            tn.write(b"conf t\n")
            tn.write(b"hostname {}\n".format(args.get("name")))
            tn.write(b"exit\n")

            print(tn.read_all())

            return {"result": args.get("name")}

@app.route("/router2_config")
def router2_config():

    HOST = "192.168.56.20"
    user = "user"
    password = "pass"

    tn = telnetlib.Telnet(HOST)

    tn.write(user.encode("ascii") + b"\n")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"router rip\n")
    tn.write(b"network 10.0.0.0\n")
    tn.write(b"network 10.0.2.0\n")

    tn.write(b"exit\n")

    print(tn.read_all())

    return {"result": "ROUTER2 is Configured"} 

@app.route("/router2_clear")
def router2_clear():

    HOST = "192.168.56.20"
    user = "user"
    password = "pass"

    tn = telnetlib.Telnet(HOST)

    tn.write(user.encode("ascii") + b"\n")
    tn.write(password.encode("ascii") + b"\n")

    tn.write(b"conf t\n")
    tn.write(b"no router rip\n")

    tn.write(b"exit\n")

    print(tn.read_all())

    return {"result": "ROUTER2 RIP Configuration is Cleared"}                                   

    
        


if __name__ == "__main__":
    app.run(debug=True, port = 8080)