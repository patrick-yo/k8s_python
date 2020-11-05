from flask import Flask
from api.list import blueprint as list_blue

__author__ = 'yan'

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(list_blue)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
