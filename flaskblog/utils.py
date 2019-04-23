from PIL import Image
import os, secrets
from flaskblog import app

def save_picture(form_picture) :
    """save picture from user form"""

    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    img = Image.open(form_picture)
    img.thumbnail((125,125))
    img.save(picture_path)
    return picture_fn
