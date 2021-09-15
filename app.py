from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import config as C
from Model import user 
app = Flask(__name__)
app.config['SECRET_KEY'] ='testkey'
# set sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = C.DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

@app.route('/register', methods=['GET','POST']) #GET(정보보기), POST(정보수정) 메서드 허용
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_2 = request.form.get('re_password')
        print(password,password_2)
        if not(name and email and password and password_2):
            return "입력되지 않은 정보가 있습니다"
        elif password != password_2:
            return "비밀번호가 일치하지 않습니다"
        else:
            usertable=user.User(email,name,password) #user_table 클래스
            usertable.email_id = email
            usertable.user_name = name
            usertable.haing_pw = usertable.pw
            
            db.session.add(usertable)
            db.session.commit()
            return "회원가입 성공"
        return "success"

if __name__ == "__main__":
    app.run(debug = True)