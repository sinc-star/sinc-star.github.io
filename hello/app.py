from flask import Flask, render_template, request
'''使用 Flask 框架构建的简单网页应用程序。'''
'''Flask 用于创建应用程序实例 render_template 用于渲染模板 request 用于处理 HTTP 请求。'''
app = Flask(__name__)
'''__name__ 参数是用于确定应用的根路径，以便 Flask 可以找到资源文件。'''
@app.route('/')
def hello():
    return render_template('hello.html')

@app.route("/", methods=['POST','GET'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', 'World')
        return render_template('greet.html', name=name)
    return render_template("hello.html")