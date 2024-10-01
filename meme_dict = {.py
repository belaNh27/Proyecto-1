meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "BANEAR": "castellanización del verbo inglés 'to ban' (expulsar). Impedir el acceso a un usuario de un foro o un sitio por parte de la administración. Generalmente un usuario es baneado por incumplimiento reiterativo de las normas del lugar.",
    "CREEPY": "aterrador, siniestro",
    "BUG": "Palabra inglesa utilizada en cualquier software para referirse a fallos en su programación.",
    "FAKE": "del Inglés, Falso. Se utiliza para engañar virtualmente a la gente por Internet",
    
"FAIL": "En español, Fallo, suele indicar una acción penosamente realizada, aunque también se usa para crear incomodidad en alguna situación real.",

"FPS": "Tiene dos significados, uno es First Person Shooter, 'Juego de Acción en Primera Persona'en español. Otro es Frames per Second, 'Fotogramas por Segundo', referente a la cantidad de imágenes por segundo de un videojuego.",

"GAMER": "Persona apasionada por los juegos, ya sean de ordenador, internet o videoconsolas.",
    
"HACKER": "Dícese de la persona que utiliza Hacks.",
    "LAG": "Dificultad producida por el retraso de una comunicación normalmente ocurrida por fallos en la conexión de internet.",
    "NOOB": "Palabra inglesa con el mismo significado que novato, usado de forma despectiva, para burlarse a alguien que tiene conocimientos inferiores.",
    "SCREAMER": "Broma de internet que tiene como objetivo asustar al usuario de forma inesperada (generalmente mediante un video) por medio de la imagen de un monstruo acompañada de un grito.",
    "SPOILER": "del inglés 'Spoil' cuyo significado literal es 'estropear(se), echar(se) a perder, etc.' Es un BBCode de los foros que oculta parte del contenido de un post, haciéndolo visible pulsando un botón.",
    "STALKER": "Del inglés, literalmente 'acosador'. En las redes sociales se llama a aquellos usuarios que rastrean, estudian, persiguen y recaban datos de otros para acosar y molestar."
}

palabras_ingresadas = {}

palabras = input("Escribe 5 palabras separadas por coma: ")

palabras_lista = [palabra.strip().upper() for palabra in palabras.split(",")]

for palabra in palabras_lista:
    if palabra in meme_dict.keys() :
        print("La palabra", palabra, "significa:", meme_dict[palabra])
    else:
        print("Lo sentimos, la palabra ingresada no se encuentra. Verifique si la escribió correctamente.")
    
    palabras_ingresadas[palabra] = "Encontrada" if palabra in meme_dict.keys() else "No encontrada"

print("\nPalabras ingresadas:")
for palabra, resultado in palabras_ingresadas.items():
    print(palabra + ": " + resultado)