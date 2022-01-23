"""
Django settings for MyDjango project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目路径
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 密钥配置
SECRET_KEY = 'django-insecure-nn++i)re32f#s%l805x38!f32am3e-12s3%x0ez%6buo*%v9jt'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
DEBUG = True

# 域名访问权限
ALLOWED_HOSTS = []

# Application definition
# App列表
INSTALLED_APPS = [
    # 内置的后台管理系统
    'django.contrib.admin',
    # 内置的用户认证系统
    'django.contrib.auth',
    # 记录项目中所有model元数据（Django的ORM框架）
    'django.contrib.contenttypes',
    # Session会话功能，用于标识当前访问网站的用户身份、记录相关用户信息
    'django.contrib.sessions',
    # 消息提示功能
    'django.contrib.messages',
    # 查找静态资源路径
    'django.contrib.staticfiles',
    # 添加项目应用index
    'index',
]

# 中间件
MIDDLEWARE = [
    # 内置的安全机制，保护用户与网站的通信安全
    'django.middleware.security.SecurityMiddleware',
    # 会话Session功能
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 添加中间件 国际化与本地化功能
    'django.middleware.locale.LocaleMiddleware',
    # 处理请求信息，规范化请求内容
    'django.middleware.common.CommonMiddleware',
    # 开启CSRF防护功能
    'django.middleware.csrf.CsrfViewMiddleware',
    # 开启内置的用户认证系统
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 开启内置的信息提示功能
    'django.contrib.messages.middleware.MessageMiddleware',
    # 防止恶意程序单击劫持
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 注册根目录和index的templates文件夹
        'DIRS': [BASE_DIR / 'templates',
                 BASE_DIR / 'index/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyDjango.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {'read_default_file': str(BASE_DIR / 'my.cnf')},
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/Allstatic/'
# 设置根目录的静态资源文件夹static
STATICFILES_DIRS = [BASE_DIR / 'static',
                    # 设置App(index)的静态资源文件夹Mystatic
                    BASE_DIR / 'index/Mystatic']

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 设置媒体路由地址信息
MEDIA_URL = '/media/'
# 获取media文件夹的完整信息
MEDIA_ROOT = BASE_DIR / 'media'
