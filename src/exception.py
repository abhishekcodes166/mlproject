import sys


def error_message_detail(error, error_detail: sys):
    _, _, tb = error_detail.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{tb.tb_lineno}] "
        f"error message [{str(error)}]"
    )
    return error_message   # ✅ THIS WAS MISSING


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message   # ✅ MUST RETURN STRING
