from app import create_app, dataBase
from app.models import User

appFlask = create_app()


@appFlask.shell_context_processor
def make_shell_context():
    return {"db": dataBase, "User": User}


if __name__ == "__main__":
    appFlask.run()
