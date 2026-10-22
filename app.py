# 导入flask
from flask import Flask, render_template, request, redirect, url_for
import os # 导入操作系统模块

app = Flask(__name__)

@app.route('/') # 这个装饰器创建主页路由
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30天Python编程挑战'
    return render_template('home.html', techs=techs, name=name, title='主页')

@app.route('/about')
def about():
    name = '30天Python编程挑战'
    return render_template('about.html', name=name, title='关于我们')

@app.route('/post')
def post():
    name = '文章'
    return render_template('post.html', name=name, title='文章')


@app.route('/result', methods=['POST'])
def result():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    old_job = request.form['old_job']
    current_job = request.form['current_job']
    country = request.form['country']
    print(first_name, last_name, old_job, current_job, country)
    result_data = {
        'first_name':first_name,
        'last_name':last_name,
        'old_job': old_job,
        'current_job': current_job,
        'country':country
    }
    return render_template('result.html', result_data = result_data, title= '结果')

@app.route('/grade')
def grade():
    return render_template('grade.html', title='成绩计算器')

@app.route('/grade/result', methods=['POST'])
def grade_result():
    subject = request.form['subject']
    score = float(request.form['score'])

    if score >= 90:
        level = '优秀！'
    elif score >= 80:
        level = '很好！'
    elif score >= 70:
        level = '一般！'
    elif score >= 60:
        level = '及格！'
    else:
        level = '你需要更加努力！'

    message = f'{level}你的{subject}成绩是{score:g}'
    return render_template('grade_result.html', message=message, title='成绩结果')

if __name__ == '__main__':
    # 部署时我们使用环境变量
    # 使其同时适用于生产和开发环境
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)