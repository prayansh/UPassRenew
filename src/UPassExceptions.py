class UPassException(Exception):
    """
    Base UPass Exception
    """

    def __init__(self, msg=None, stacktrace=None):
        self.msg = msg
        self.stacktrace = stacktrace

    def __str__(self):
        exception_msg = "Message: %s\n" % self.msg
        if self.stacktrace is not None:
            stacktrace = "\n".join(self.stacktrace)
            exception_msg += "Stacktrace:\n%s" % stacktrace
        return exception_msg


class CredentialsNotFound(UPassException):
    pass


class NothingToRenew(UPassException):
    pass


class InvalidCredentials(UPassException):
    def __init__(self, msg=None, stacktrace=None, user=None):
        UPassException.__init__(self, msg, stacktrace)
        self.user = user
