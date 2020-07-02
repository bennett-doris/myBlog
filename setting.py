# -*- coding: utf-8 -*-
# 使用Python类组织配置
# 分别配置 基本配置类(BaseConfig) 测试配置类(TestConfig) 开发配置类(DevelopmentConfig) 生产配置类(ProductionConfig)

import os

# 获取项目路径：先获取脚本所在的完整的绝对路径，然后去掉文件名，保留绝对路径的目录名，再获取该目录名的绝对路径
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 配置基本配置类
class BaseConfig(object):
    # 设置安全验证
    # os.getenv() 获取一个环境变量，如果没有返回none
    SECRET_KEY = os.getenv('SECRET_KEY','secret string')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置邮件服务器环境
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('myBlog Admin',MAIL_USERNAME)

    MYBLOG_EMAIL = os.getenv('MYBLOG_EMAIL')
    MYBLOG_POST_PER_PAGE = 10
    MYBLOG_MANAGE_POST_PER_PAGE = 15
    MYBLOG_COMMENT_PER_PAGE = 15

# 配置开发环境
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/blog'

# 配置测试环境
class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/testblog'

# 配置生产环境
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/problog'

# 创建一个存储配置名称和对应配置类的字典，用于在创建程序实例时通过配置名称来获取对应的配置类
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig
}