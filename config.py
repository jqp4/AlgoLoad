import os

# Почему-то не грузится dotenv
# from dotenv import load_dotenv

# Папка для хранения базы данных по умолчанию
basedir = os.path.abspath(os.path.dirname(__file__))
# Почему-то не грузится dotenv
# load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    FLUTTER_APP_BASE_URL_DEV = "http://localhost:56912"
    FLUTTER_APP_BASE_URL_STAGING = "https://jqp4.github.io/algoload-flutter-demo"
    FLUTTER_APP_BASE_URL_PROD = "http://localhost:54026"  # todo: replace

    # Ключ безопасности - защита от CSRF
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"

    # todo: clean

    # Решение (?) проблем с werkzeug.exceptions.NotFound
    # https://github.com/apache/superset/issues/20319
    SESSION_COOKIE_SAMESITE = "Lax"
    # SESSION_COOKIE_HTTPONLY = True

    # SESSION_COOKIE_SAMESITE = "None"
    # SESSION_COOKIE_SECURE = True

    # new
    SESSION_COOKIE_HTTPONLY = False
    # REMEMBER_COOKIE_HTTPONLY = False

    # База данных
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "volume/app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Отправка ошибок по почте
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["test@gmail.com"]
