# -*- coding: utf-8 -*-
from flask import Blueprint

# 蓝本对象实例化
# 蓝本对象构造方法，第一个参数是蓝本的名称，第二个参数是包或模块的名称，可以用 __name__ 变量
auth_bp = Blueprint('auth',__name__)

# 登录函数
@auth_bp.route('/login')
def login():
    pass

# 注销函数
@auth_bp.route('/logout')
def logout():
    pass
