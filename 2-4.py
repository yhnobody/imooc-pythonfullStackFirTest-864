# -*- encoding:utf-8 -*-  

from flask import Flask   ### 导出 Flask 类
app = Flask(__name__)     ### 生成一个web app 对象

@app.route('/')           ### 注册一个url， 表示当请求url+‘/’这个网址时，执行 hello_world这个函数
def hello_world():
    return 'Hello ， every one'

if __name__ == '__main__': ### 启动这个app 应用
    app.run()              ### 相关参数： app.run(host-None, port-None, debug-None, **aptions)
                           ### host 默认是： 127.0.0.1
                           ### port 默认是： 5000