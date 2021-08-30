from enums import lost_param_err
from tools.bind import bind_param, bind_json


class Base:
    def _required_verify(self):
        pass

    def required(self, required_list: list = None):
        if required_list:
            if not all([getattr(self, i) for i in required_list]):
                return lost_param_err

    def _verify(self):
        pass

    def _bind(self):
        return bind_param(self)

    def check_param(self):
        if err := self._bind():
            return err
        if err := self._required_verify():
            return err
        return self._verify()
