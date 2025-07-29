from dotenv import load_dotenv
import os

load_dotenv()
class Config:
    usuario_correcto = os.getenv("usuario_correcto")
    usuario_incorrecto = os.getenv("usuario_incorrecto")
    pass_correcto = os.getenv("pass_correcto")
    pass_incorrecto = os.getenv("pass_incorrecto")
    user_formato_incorrecto = os.getenv("user_formato_incorrecto")
    URL = os.getenv("URL")

   