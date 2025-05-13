from flask import session
from app import create_app

app = create_app()

@app.before_request
def before_request_func():
    print("Running before_request...")
    session['msg'] = False
    session['messages']=[]
    session['conf'] = False
    session['confirm'] = ""
    session['confirmroute'] = ""
    session['cancel'] = False

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
