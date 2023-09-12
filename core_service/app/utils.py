import inspect
import uuid
def retrieve_var_name() -> str:
    """Retrieve variable name from the caller's scope which code not start with
    space."""
    frames = inspect.getouterframes(inspect.currentframe())

    for f in frames[1:]:  # Skip the current frame
        code_ctx = f.code_context
        if code_ctx is not None and not code_ctx[0].startswith(" "):
            return code_ctx[0].split("=")[0].strip()
    msg = "Cannot find variable name"
    raise ValueError(msg)

def generate_string_uuid():
    return uuid.uuid4().hex

def map_db_model_to_dict(db_model) -> dict:
    data_dict = {k: v for k, v in db_model.__dict__.items()}
    return data_dict