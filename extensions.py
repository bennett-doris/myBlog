# -*- coding: utf-8 -*-
# 用来存储扩展实例化等操作

from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor
from flask_moment import Moment

# 可供在工厂函数中导入扩展对象，并调用init_app()方法，传入程序实例初始化操作
bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
ckeditor = CKEditor()
mail = Mail()