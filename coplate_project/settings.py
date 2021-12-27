"""
Django settings for coplate_project project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&bpm0den)^q4o39@5s)1x7oof=qp)*x6m7p=%@_!ex#y+n=)6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [".run.goorm.io"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'coplate', #coplate가 allauth보다 위에 있어야 템플릿 오버라이딩 가능
    'widget_tweaks', #input 태그 수정하기 위한 패키지
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'coplate.middleware.ProfileSetupMiddleware',
]

ROOT_URLCONF = 'coplate_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'coplate_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME" : "coplate.validators.CustomPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/uploads/"

#Auth Setting

AUTH_USER_MODEL = "coplate.User"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_REDIRECT_URL = 'profile-set'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'account_login'
ACCOUNT_LOGOUT_ON_GET = True #로그아웃 누르면 바로 로그아웃되기
ACCOUNT_AUTHENTICATION_METHOD = 'email' #email로 로그인하기
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False #로그인에 username 쓰는 필드 없애기
# ACCOUNT_SIGNUP_FORM_CLASS = "coplate.forms.SignupForm"
ACCOUNT_SESSION_REMEMBER = True #브라우저 닫아도 세션쿠키 지우지 않도록 설정
# SESSION_COOKIE_AGE = 3600 세션쿠키 유지시간. 디폴트는 2주. 단위는 초
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True #회원가입시 비밀번호는 제대로 입력해도 다른거때매 유효성검사 통과 못한경우 비밀번호는 그대로 남겨두기
# ACCOUNT_EMAIL_VARIFICATION = "mandatory" #이메일 인증할 때 까지 가입 못함
ACCOUNT_CONFIRM_EMAIL_ON_GET=True #이메일 인증링크로 들어갔을 때 바로 인증되게 하기
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'account_email_confirmation_done'#로그인 됐을때
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'account_email_confirmation_done'#로그인 안됐을때
PASSWORD_RESET_TIMOUT = 3600
ACCOUNT_EMAIL_SUBJECT_PREFIX='' #이메일 제목에 도메인 붙는거 제거하기


#Email settings

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

