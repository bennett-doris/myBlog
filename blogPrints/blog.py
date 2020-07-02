# -*- coding: utf-8 -*-
from flask import Blueprint

# 蓝本对象实例化
# 蓝本对象构造方法，第一个参数是蓝本的名称，第二个参数是包或模块的名称，可以用 __name__ 变量
blog_bp = Blueprint('blog',__name__)
