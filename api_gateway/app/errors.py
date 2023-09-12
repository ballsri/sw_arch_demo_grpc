from fastapi import HTTPException

import app.utils as utils


class HTTPExceptionWithCode(HTTPException):
    status_code: int = 0
    error_code: str = ""
    detail: str = ""

    def __init__(self, more_detail: str = "") -> None:
        if more_detail:
            detail = f"{self.detail}: {more_detail}"
        else:
            detail = self.detail
        super().__init__(status_code=self.status_code, detail=detail)


def _Error(status_code: int, error_code: str, detail: str):
    type_name = utils.retrieve_var_name()
    return type(
        type_name,
        (HTTPExceptionWithCode,),
        {"status_code": status_code, "error_code": error_code, "detail": detail},
    )


HouseKeeperNotFoundError = _Error(
    status_code=404, error_code="DEMO-001", detail="House keeper not found"
)
