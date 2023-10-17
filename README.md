Modelo de Embeddings para Películas
Este repositorio contiene un modelo de embeddings basado en la librería Transformers de Hugging Face que se utilizó para procesar un dataset de películas. Los embeddings generados a partir de este modelo se cargaron en una base de datos vectorial para permitir consultas eficientes sobre películas.

Resumen
El objetivo de este proyecto es aprovechar las poderosas capacidades de los modelos de lenguaje pre-entrenados para generar representaciones vectoriales (embeddings) de películas a partir de descripciones de texto. Estas representaciones vectoriales se utilizan para construir una base de datos vectorial que permite realizar búsquedas similares a través de consultas.

Cómo se utilizó el modelo
Modelo Pre-Entrenado: Para generar los embeddings, se utilizó un modelo de lenguaje pre-entrenado de la librería Transformers de Hugging Face. Este modelo se ajustó específicamente para procesar descripciones de películas.

Procesamiento del Dataset: Se preparó un dataset que contiene datos de películas, incluyendo títulos, resúmenes y otros atributos relevantes. El modelo pre-entrenado se utilizó para generar representaciones vectoriales para cada entrada del dataset.

Subida a una Base de Datos Vectorial: Los embeddings generados se subieron a una base de datos vectorial compatible con Pinecone. Esto permite almacenar y recuperar eficientemente las representaciones vectoriales de las películas.

Consulta de Películas: Se desarrolló una función de consulta que utiliza la base de datos vectorial para buscar películas similares a una consulta dada. Esta función permite realizar consultas basadas en el contenido de las películas y otros criterios como género y calificación.

Requisitos
Antes de utilizar este proyecto, asegúrate de que tienes instaladas las siguientes bibliotecas:

Transformers de Hugging Face
Pinecone (para la base de datos vectorial)
Puedes instalar estas bibliotecas usando pip


Uso
Para utilizar este proyecto, sigue estos pasos:

Entrenamiento del Modelo: Utiliza el modelo pre-entrenado de Transformers para generar embeddings a partir de tus datos de películas.

Subida a la Base de Datos Vectorial: Utiliza la base de datos vectorial Pinecone para subir los embeddings generados.

Consulta de Películas: Utiliza la función de consulta proporcionada para buscar películas similares en la base de datos vectorial.

Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor crea un pull request.