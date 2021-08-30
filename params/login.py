from . import Base
from enums import lost_param_err


class UserLoginParam(Base):
    key = ""
    password = ""

    def _required_verify(self):
        if not all([self.key, self.password]):
            return lost_param_err
