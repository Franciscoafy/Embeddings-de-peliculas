


def search(query, genre, rating, top_k):
    # 1. Encodeamos la consulta de búsqueda en un vector utilizando un modelo previamente entrenado (no se muestra la definición de 'model' en el código).

    query_vector = model.encode(query).tolist()

    # 2. Configuramos las condiciones de filtrado basadas en el género y la calificación.
    if rating:
        filter_rating = rating #si nos dan un rating lo seleccionamos
    else:
        filter_rating = 0# sino que el rating sea 0

    if genre:
        conditions = {
            "Generes": { "$in": [genre] },
            "Rating": { "$gte": filter_rating }
        }
    else:
        conditions = {
            "Rating": { "$gte": filter_rating }
        }

    # 3. Realizamos una consulta en la base de datos vectorial de Pinecone utilizando el vector de consulta y las condiciones de filtrado.
    responses = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True,
        filter=conditions
    )

    # 4. Formateamos las respuestas para su visualización.
    response_data = []
    for response in responses['matches']:
        response_data.append({
            'Title': response['metadata']['movie title'],
            'Overview': response['metadata']['Overview'],
            'Director': response['metadata']['Director'],
            'Genre': response['metadata']['Generes'],
            'Year': response['metadata']['year'],
            'Rating': response['metadata']['Rating'],
            'Score': response['score'],
        })

    # 5. Creamos un DataFrame de pandas a partir de los datos formateados y lo devuelve como resultado.
    df = pd.DataFrame(response_data)
    return df


def concatenar_lista(lista):
    # Convertimos la cadena de entrada en una lista de Python utilizando literal_eval.
    lista = literal_eval(lista)

    # Usamos el método join para concatenar los elementos de la lista en una cadena de texto.
    # Se utiliza un espacio como separador entre los elementos.
    return ' '.join(lista)


def string_to_list(lista):

    lista = literal_eval(lista)
    return lista