"""DSM 5 SYNO.API.Auth data."""
from tests.const import (
    SESSION_ID,
    DEVICE_TOKEN,
    ERROR_AUTH_OTP_NOT_SPECIFIED,
)

# No synotoken for an unknown reason
DSM_5_AUTH_LOGIN = {
    "data": {"is_portal_port": False, "sid": SESSION_ID},
    "success": True,
}
DSM_5_AUTH_LOGIN_2SA = ERROR_AUTH_OTP_NOT_SPECIFIED
DSM_5_AUTH_LOGIN_2SA_OTP = {
    "data": {"did": DEVICE_TOKEN, "is_portal_port": False, "sid": SESSION_ID},
    "success": True,
}
