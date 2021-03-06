

class UnknownHostException(Exception):
    """Raised when a host is unknown (dns failure)"""
    pass


class ConnectionErrorException(Exception):
    """Raised on error connecting (connection refused/timed out)"""
    pass


class AuthenticationException(Exception):
    """Raised on authentication error (user/password/ssh key error)"""
    pass


class SessionError(Exception):
    """Raised on errors establishing SSH session"""
    pass


class PKeyFileError(Exception):
    """Raised on errors finding private key file"""
    pass
