from models.base_model import BaseModel


class PostLike(BaseModel):
    post_id: str
    user_id: str
