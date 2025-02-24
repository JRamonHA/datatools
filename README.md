# DataTools

`datatools` es un paquete de Python diseñado para facilitar el análisis y la verificación de datos en archivos CSV. Este paquete es ideal para tareas de limpieza y validación de datos, especialmente cuando se trabaja con múltiples archivos o grandes conjuntos de datos.

## Tabla de contenidos
- [Instalación](#instalación)
- [Uso](#uso)
  - [Comparar Columnas de Archivos](#comparar-columnas-de-archivos)
  - [Verificar Tipos de Datos de Columnas](#verificar-tipos-de-datos-de-columnas)
  - [Detectar Filas Duplicadas](#detectar-filas-duplicadas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Instalación

Para instalar `datatools`, asegúrate de tener Python 3.6 o superior y la biblioteca Pandas instalada. Puedes instalar el paquete a través de este comando:
```bash
pip install git+https://github.com/JRamonHA/datatools.git
```

### Requisitos
- Python 3.6+
- Pandas

### Uso
Una vez instalado, puedes importar el paquete y usar sus funciones directamente:
```bash
import datatools as dt
```

#### Comparar columnas de archivos

La función `compare` lee todos los archivos con una extensión específica en un directorio dado y compara las columnas de cada archivo con las del primer archivo, que se usa como referencia.

```bash
dt.compare(path, extension)
```

- Parámetros:
    - path (str): Ruta del directorio que contiene los archivos​.
    - extension (str): Extensión de los archivos a leer (por ejemplo, 'csv').
    - Retorno: Imprime los resultados de la comparación en la consola.

#### Verificar tipos de datos de columnas

La función `column_type` verifica si los tipos de datos de las columnas en un DataFrame coinciden con los tipos esperados.

```bash
dt.column_type(columns_expected_type, data)
```

- Parámetros:
    - columns_expected_type (dict): Diccionario con nombres de columnas como claves y tipos de datos esperados como valores (en formato de cadena, por ejemplo, 'float64').
    - data (pandas.DataFrame): DataFrame a verificar.
    - Retorno: Imprime discrepancias si los tipos no coinciden.

#### Detectar filas duplicadas
La función `duplicate_rows` verifica si hay filas duplicadas en un DataFrame basado en sus índices.

```bash
dt.duplicate_rows(data)
```

### Contribuciones
Si deseas contribuir a este paquete, puedes hacerlo mediante pull requests en el repositorio oficial. Asegúrate de seguir las mejores prácticas de codificación y de incluir pruebas para cualquier nueva funcionalidad.

Para reportar problemas o sugerir mejoras, por favor abre un issue en el repositorio.

### Licencia
Este paquete está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
