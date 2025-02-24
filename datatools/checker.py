import pandas as pd
import glob

def compare(path, extension):
    """
    Lee todos los archivos con una extensión específica en el directorio dado,
    y compara las columnas de cada archivo con las del primer archivo leído, que se usa como referencia.
    
    Args:
        path (str): Ruta del directorio que contiene los archivos CSV.
        extension (str): Extensión de los archivos a leer (por ejemplo, 'csv').
    
    Returns:
        None: La función imprime los resultados de la comparación de columnas en la consola.
    """
    # Obtiene todos los archivos con la extensión indicada en el directorio especificado
    files = glob.glob(f'{path}/*.{extension}')
    
    # Diccionario para almacenar columnas de cada archivo
    file_columns = {}

    for file in files:
        # Si el nombre del archivo contiene "2022" o "2023", se lee sin skiprows
        if "2022" in file or "2023" in file:
            df = pd.read_csv(file, encoding='ANSI', index_col=0, parse_dates=True, low_memory=False)
        else:
            df = pd.read_csv(file, encoding='ANSI', skiprows=[0, 2, 3],
                             index_col=0, parse_dates=True, dayfirst=True, low_memory=False)
        
        # Almacena las columnas del DataFrame
        file_columns[file] = set(df.columns)
    
    # Compara columnas entre archivos usando el primero como referencia
    reference_columns = None
    for file, columns in file_columns.items():
        if reference_columns is None:
            reference_columns = columns
            print(f"\n{file} se usa como referencia con columnas: \n{columns}")
        else:
            # Calcula las columnas comunes y las diferencias
            common = reference_columns.intersection(columns)
            missing = reference_columns.difference(columns)  # Columnas que faltan en el archivo actual
            extra = columns.difference(reference_columns)    # Columnas que tiene el archivo actual de más

            print(f"\nComparación para {file}:")
            print(f"Columnas comunes: {common}")
            print(f"Columnas faltantes (en referencia): {missing}")
            print(f"Columnas extra (en archivo): {extra}")

            if columns == reference_columns:
                print(f"{file} coincide con la referencia.")
            else:
                print(f"{file} no coincide con la referencia.")

def column_type(columns_expected_type, data):
    """
    Verifica que los tipos de datos de las columnas en un DataFrame coincidan con los tipos esperados.
    
    Args:
        columns_expected_type (dict): Un diccionario donde las claves son los nombres de las columnas,
                                      y los valores son los tipos de datos esperados como cadenas de texto.
        data (pandas.DataFrame): El DataFrame que contiene los datos a verificar.
    
    Returns:
        None: La función imprime un mensaje si hay discrepancias entre los tipos esperados y los obtenidos.
    """
    columns_obtained_type = {columna: f'{data[columna].dtype}' for columna in data.columns}

    for key in set(columns_expected_type.keys()).union(columns_obtained_type.keys()):
        expected = columns_expected_type.get(key, None)
        obtained = columns_obtained_type.get(key, None)
        
        if expected != obtained:
            print(f"En la columna '{key}' se espera: {expected}\nPero se obtuvo: {obtained}")

def duplicate_rows(data):
    """
    Verifica si hay filas duplicadas en un DataFrame basado en sus índices.
    
    Args:
        data (pandas.DataFrame): El DataFrame a verificar.
    
    Returns:
        None: Si hay filas duplicadas, imprime los índices duplicados y las filas correspondientes.
    """
    if data.index.duplicated().any():
        # Obtiene todos los índices duplicados (incluye todas las ocurrencias)
        duplicated_indexes = data.index[data.index.duplicated(keep=False)]
        print("Índices duplicados:")
        print(duplicated_indexes.unique())
        
        # Muestra todas las filas cuyos índices están duplicados
        duplicated_rows = data.loc[duplicated_indexes]
        print("\nFilas duplicadas:")
        print(duplicated_rows.to_string())