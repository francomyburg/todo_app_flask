from crypt import methods
from flask import Flask,render_template,request,redirect,url_for


todos = [{"name":"clean bedroom"},{"name":"clean kitchen"}]


app=Flask(__name__,template_folder="templates")


@app.route("/")
def home():
    return render_template("home.html",todos=todos)

@app.route("/add",methods=["POST"])
def add():
    todo=request.form['name']
    todos.append({'name':todo,'done':False})
    return redirect(url_for("home"))

@app.route("/edit/<int:index>",methods=['GET','POST'])
def edit(index):
    todo=todos[index]
    if request.method == 'POST':
        todo['name'] =  request.form['name']
        return redirect(url_for('home'))
    else:
        return render_template('edit.html',todo=todo,index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('home'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run("127.0.0.1",5000,True)