from models.base_model import BaseModel


class Advertisement(BaseModel):
    meta_data: dict
    post_id: str
    user_id: str
