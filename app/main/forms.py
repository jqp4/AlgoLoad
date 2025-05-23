from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User

from flask import request
from wtforms.fields.html5 import URLField


class EditProfileForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField("Номер варианта", validators=[DataRequired()])
    about_me = TextAreaField("Контактные данные", validators=[Length(min=0, max=140)])
    local_folder = TextAreaField("Локальный путь", validators=[Length(min=0, max=140)])
    submit = SubmitField("Изменить")

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError("Имя пользователя уже занято.")


class TaskSubmitForm(FlaskForm):
    class Meta:
        csrf = False

    task_code = TextAreaField(
        "Комментарий к заданию", validators=[Length(min=0, max=16384)]
    )
    file_data = FileField(
        "Загрузить описание графа",
        validators=[
            FileRequired(),
            FileAllowed(["xml", "json", "cpp"], "XML/JSON/CPP описания."),
        ],
    )  # json для дебага C++ скрипта

    submit = SubmitField("Сгенерировать")

    def __init__(self, *args, **kwargs):
        super(TaskSubmitForm, self).__init__(*args, **kwargs)


class TaskReceiveForm(FlaskForm):
    class Meta:
        csrf = False

    task_code = TextAreaField(
        "Комментарий к результату", validators=[Length(min=0, max=16384)]
    )

    def __init__(self, *args, **kwargs):
        super(TaskReceiveForm, self).__init__(*args, **kwargs)
        # Проинициализировать здесь результирующие данные


class ReportSubmitForm(FlaskForm):
    class Meta:
        csrf = False

    file_data = FileField(
        "Загрузить новый отчет",
        validators=[
            FileRequired(),
            FileAllowed(["docx", "doc", "pdf"], "Только документы срасширением .docx!"),
        ],
    )
    submit = SubmitField("Отправить")

    def __init__(self, *args, **kwargs):
        super(ReportSubmitForm, self).__init__(*args, **kwargs)
