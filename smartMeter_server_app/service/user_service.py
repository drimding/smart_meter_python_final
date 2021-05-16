from flask_jwt_extended import get_jwt_identity
from sqlalchemy.exc import IntegrityError, DataError

from smartMeter_server_app import db, login_manager
from smartMeter_server_app.models.user_model import User
from smartMeter_server_app.schemas.user_schema import UserSchema


class UserService:
    @login_manager.user_loader
    def load_user(self):
        return db.session.query(User).filter_by(uuid=self).first()

    @staticmethod
    def add(user: User):
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            return {"message": "Such user exists"}, 409
        except DataError:
            return {"message": "Wrong data"}, 413
        user_schema = UserSchema()
        return user_schema.dump(user), 201

    @staticmethod
    def get_bu_username(username):
        user = db.session.query(User).filter_by(username=username).first()
        return user

    @staticmethod
    def get_by_uuid(uuid):
        user = db.session.query(User).filter_by(uuid=uuid).first()
        return user

    @staticmethod
    def get_current_user():
        return UserService.get_by_uuid(get_jwt_identity())

    @staticmethod
    def delete_user(user: User):
        db.session.delete(user)
        db.session.commit()
        return '', 204
