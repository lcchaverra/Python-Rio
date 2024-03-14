#pip install -r requirements.txt
#py -m pip
# uvicorn main:app --reload
import sqlite3
import fastapi
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel
import random as random

app = fastapi.FastAPI()

conexion = sqlite3.connect("netflix.db")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def raiz():
    return "Backend de Python + Fastapi + SQLite"

class LoginData(BaseModel):
    username: str
    password: str

class ShopData(BaseModel):
    username: str
    email: str
    phone: str
    address: str
    count: float
    total: float

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

@app.post("/create")
async def crear_usuario(data: LoginData):
    username = data.username
    password = data.password
    id = random.randint(1, 100)
    cursor = conexion.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (id, usuario, contraseña) VALUES(?,?,?)', (id, username, password))
        conexion.commit()
        return {"status": "success", "message": "nuevo_usuario creado"}
    except:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    # finally:
        # conexion.close()

@app.post("/complete_shopping")
async def completar_compra(data: ShopData):
    username = data.username
    email = data.email
    phone = data.phone
    address = data.address
    count = data.count
    total = data.total
    cursor = conexion.cursor()
    try:
        cursor.execute('INSERT INTO pedidos (username, email, phone, address, count, total) VALUES(?,?,?,?,?,?)', (username, email, phone, address, count, total))
        conexion.commit()
        return {"status": "success", "message": "compra realizada"}
    except:
        raise HTTPException(status_code=401, detail="no se pudo realizar la compra")
    # finally:
        # conexion.close()