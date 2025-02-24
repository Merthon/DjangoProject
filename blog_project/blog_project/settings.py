import os
from pathlib import Path

# BASE_DIR 用于构建相对于项目根目录的路径
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: 请确保保密此密钥，在生产环境中使用环境变量管理
SECRET_KEY = 'your-secret-key-here'

# DEBUG 设置：生产环境下应设为 False
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# 应用注册：包含 Django 内置应用和我们自定义的 blog 应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # 注册博客应用
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF 防护中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog_project.urls'

# 模板配置：自动寻找各应用中的 templates 目录
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 全局模板目录（可选）
        'APP_DIRS': True,  # 自动搜索各应用下的 templates 目录
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # 使 request 对象在模板中可用
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog_project.wsgi.application'

# 数据库配置：使用 MySQL 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 指定使用 MySQL 数据库引擎
        'NAME': 'blog_db',                     # 数据库名称
        'USER': 'root',             # 数据库用户名
        'PASSWORD': 'root',     # 数据库密码
        'HOST': 'localhost',                   # 数据库服务器地址
        'PORT': '3306',                        # 数据库端口
    }
}

# 密码验证配置
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国际化配置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静态文件配置（CSS、JavaScript、图片等）
STATIC_URL = '/static/'

# 默认主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
