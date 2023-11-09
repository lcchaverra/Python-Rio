#pip install -r requirements.txt
#py -m pip
# uvicorn main:app --reload
# import datetime as dt

# @app.post("/login")
# async def validar_datos(request: Request):
#     datos = await request.json()
#     return {"Datos recibidos correctamente: "+ datos}

# users_db = {
#     "lucas.cordoba1510@gmail.com": {"password": "123456"},
#     "usuario2": {"password": "contraseña2"},
# }


# @app.get("/create")
# async def crear_usuario():
#     cursor = conexion.cursor()
#     cursor.execute('INSERT INTO usuarios (id, usuario, contraseña) VALUES(4, "josser@gmail.com", "123456")')
#     conexion.commit()
#     conexion.close()
#     return "nuevo_usuario creado"

# @app.get("/movies")
# async def listado_peliculas():
#     datos = traer_datos("SELECT * FROM peliculas")
#     return datos

# @app.get("/movies/{movie_id}")
# async def cargar_peliculas(movie_id : str | None = None):
#     if movie_id is not None:
#         datos = traer_datos("SELECT * FROM usuarios WHERE id ="+ movie_id+"")
#     else:
#         datos = traer_datos("SELECT * FROM peliculas")
#     return datos


# @app.get("/watch/{content_id}")
# async def watch_content(content_id: str):
#     result = [m for m in MOVIES if str(m["id"]) == content_id][0]
#     return result

    # peticiones('CREATE TABLE IF NOT EXISTS usuarios ( id INTEGER PRIMARY KEY, usuario TEXT NOT NULL, contraseña TEXT NOT NULL)')
    # peticiones('INSERT INTO usuarios VALUES (1, "lcchaverra", "123456")')
    # peticiones('INSERT INTO usuarios VALUES (2, "admin", "123456789")')
# MOVIES = [
#     {
#         "id": 120,
#         "original_language": "English",
#         "overview": "Young hobbit Frodo Baggins, after inheriting a mysterious ring from his uncle Bilbo, must leave his home in order to keep it from falling into the hands of its evil creator. Along the way, a fellowship is formed to protect the ringbearer and make sure that the ring arrives at its final destination: Mt. Doom, the only place where it can be destroyed.",
#         "poster_path": "/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg",
#         "release_date": "2001-12-18",
#         "runtime": 179,
#         "tagline": "One ring to rule them all",
#         "title": "The Lord of the Rings: The Fellowship of the Ring",
#         "certification": "PG-13",
#         "trailer": "https://www.youtube.com/watch?v=V75dMMIW2B4",
#     },
#     {
#         "id": 603,
#         "original_language": "English",
#         "overview": "Set in the 22nd century, The Matrix tells the story of a computer hacker who joins a group of underground insurgents fighting the vast and powerful computers who now rule the earth.",
#         "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
#         "release_date": "1999-03-30",
#         "runtime": 136,
#         "tagline": "Welcome to the Real World.",
#         "title": "The Matrix",
#         "certification": "R",
#         "trailer": "https://www.youtube.com/watch?v=m8e-FF8MsqU",
#     },
#     {
#         "id": 1368,
#         "original_language": "English",
#         "overview": "When former Green Beret John Rambo is harassed by local law enforcement and arrested for vagrancy, the Vietnam vet snaps, runs for the hills and rat-a-tat-tats his way into the action-movie hall of fame. Hounded by a relentless sheriff, Rambo employs heavy-handed guerilla tactics to shake the cops off his tail.",
#         "poster_path": "/fVamGe8rfEQUrMbzumL1t0DslCA.jpg",
#         "release_date": "1982-10-22",
#         "runtime": 93,
#         "tagline": "This time he's fighting for his life.",
#         "title": "First Blood",
#         "certification": "R",
#         "trailer": "https://www.youtube.com/watch?v=IAqLKlxY3Eo",
#     },
#     {
#         "id": 218,
#         "original_language": "English",
#         "overview": 'In the post-apocalyptic future, reigning tyrannical supercomputers teleport a cyborg assassin known as the "Terminator" back to 1984 to kill Sarah Connor, whose unborn son is destined to lead insurgents against 21st century mechanical hegemony. Meanwhile, the human-resistance movement dispatches a lone warrior to safeguard Sarah. Can he stop the virtually indestructible killing machine?',
#         "poster_path": "/qvktm0BHcnmDpul4Hz01GIazWPr.jpg",
#         "release_date": "1984-10-26",
#         "runtime": 108,
#         "tagline": "Your future is in his hands.",
#         "title": "The Terminator",
#         "certification": "R",
#         "trailer": "https://www.youtube.com/watch?v=k64P4l2Wmeg",
#     },
# ]

# USERS = [
#     {
#     "id": 1,
#     "username": "Luis Carlos",
#     "profile": "no hay :3",
#     "estado": 1,
#     },
#     {
#     "id": 2,
#     "username": "Aguacate legendario",
#     "profile": "no hay :3 x2",
#     "estado": 0,
#     },
# ]

# @app.get("/movies")
# async def search_movies(since: dt.date | None = None, q: str | None = None):
#     result = MOVIES
#     if q is not None:
#         result = [m for m in result if q in m["overview"].lower()]

#     if since is not None:
#         result = [
#             m for m in result if since <= dt.date.fromisoformat(m["release_date"])
#         ]

#     return result


# @app.get("/watch/{content_id}")
# async def watch_content(content_id: str):
#     result = [m for m in MOVIES if str(m["id"]) == content_id][0]
#     return result

# @app.get("/users/{user_id}")
# async def user_data_watch(user_id : str | None = None):
#     if user_id is not None:
#         result = [user for user in USERS if str(user["id"]) == user_id ][0]
#     return result

# @app.get("/users")
# async def all_user_data_watch():
#     result = USERS
#     return result

# @app.get("/consulta")
# async def bd_data():
#     result = consultar("select * from users")
#     return result
