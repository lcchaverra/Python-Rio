#pip install -r requirements.txt
#py -m pip
# uvicorn main:app --reload
import sqlite3
import fastapi
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel

app = fastapi.FastAPI()

conexion = sqlite3.connect("netflix.db")

origins = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def peticiones(sql):
    conexion = sqlite3.connect("netflix.db")
    cursor = conexion.cursor()
    cursor.execute(str(sql))
    conexion.commit()
    conexion.close()

def traer_datos(sql):
    conexion = sqlite3.connect("netflix.db")
    cursor = conexion.cursor()
    cursor.execute(str(sql))
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    datos_json = [dict(zip([column[0] for column in cursor.description], fila)) for fila in datos]
    datos_json_str = json.dumps(datos_json)
    return datos_json_str

@app.get("/")
async def raiz():
    return "Hola"

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(data: LoginData):
    username = data.username
    password = data.password

    cursor = conexion.cursor()
    cursor.execute("SELECT contraseña FROM usuarios WHERE usuario=?", (username,))
    resultado = cursor.fetchone()

    if resultado is not None and resultado[0] == password:
        return {"status": "success", "message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

@app.get("/users")
async def listado_usuarios():
    datos = traer_datos("SELECT * FROM usuarios")
    return datos

@app.get("/users/{user_id}")
async def usuario_id(user_id : str | None = None):
    if user_id is not None:
        datos = traer_datos("SELECT * FROM usuarios WHERE id ="+ user_id+"")
    return datos
