from . import Base
from enums import lost_param_err


class UserSaveParam(Base):
    user_name = ""
    password = ""
    mobile = ""

    def _required_verify(self):
        if not all([self.user_name, self.password, self.mobile]):
            return lost_param_err


class UserEditParam(Base):
    user_name = ""
    mobile = ""

    def _required_verify(self):
        if not all([self.user_name, self.mobile]):
            return lost_param_err


class UserPasswordParam(Base):
    password = ""

    def _required_verify(self):
        if not self.password:
            return lost_param_err
