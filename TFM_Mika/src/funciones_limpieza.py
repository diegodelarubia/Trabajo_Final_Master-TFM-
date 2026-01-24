from IPython.display import display

# FUNCIÓN PARA HACER UN CHECK INICIAL DEL DATAFRAME

def check_df(df, tipo=''):
    if tipo == 'simple':
        print("¿Cuántas filas y columnas hay en el conjunto de datos?")
        num_filas, num_columnas = df.shape
        print("\tHay {:,} filas y {:,} columnas.".format(num_filas, num_columnas))

        print("¿Cuáles son las primeras dos filas del conjunto de datos?")
        display(df.head(2))
        print('\n########################################################################################')
    else:
        print("¿Cuántas filas y columnas hay en el conjunto de datos?")
        num_filas, num_columnas = df.shape
        print("\tHay {:,} filas y {:,} columnas.".format(num_filas, num_columnas))
        print('\n########################################################################################')

        print("¿Cuáles son las primeras cinco filas del conjunto de datos?")
        display(df.head())
        print('\n########################################################################################')

        print("¿Cuáles son las últimas cinco filas del conjunto de datos?")
        display(df.tail())
        print('\n########################################################################################')

        print("¿Cómo puedes obtener una muestra aleatoria de filas del conjunto de datos?")
        display(df.sample(n = 5))
        print('\n########################################################################################')

        print("¿Cuáles son las columnas del conjunto de datos? ¿Cuál es el tipo de datos de cada columna?")
        print(df.dtypes)
        print('\n########################################################################################')

        print("¿Cuántas columnas hay de cada tipo de datos?")
        print(df.dtypes.value_counts())
        print('\n########################################################################################')

        print("¿Cuáles son las variables numéricas?")
        df_numericas = df.select_dtypes(include = 'number')
        columnas_numericas = list(df_numericas.columns)
        print(columnas_numericas)
        print('\n########################################################################################')

        print("¿Cuáles son las variables categóricas?")
        df_categoricas = df.select_dtypes(include = 'object')
        columnas_categoricas = list(df_categoricas.columns)
        print(columnas_categoricas)
        print('\n########################################################################################')

        print("¿Cuántos valores únicos tiene cada columna?")
        print(df.nunique())
        print('\n########################################################################################')

        if len(columnas_numericas)>0:
            print("¿Cuáles son las estadísticas descriptivas básicas de las columnas numéricas?")
            display(df.describe(include = 'number'))
            print('\n########################################################################################')

        if len(columnas_categoricas)>0:
            print("¿Cuáles son las estadísticas descriptivas básicas de las columnas categóricas?")
            display(df.describe(include = 'object'))

# FUNCIÓN PARA DETECTAR VALORES PROBLEMÁTICOS

def valores_problem(df, columnas=[]):
    print('###################################################################################')
    print('3.1.1. Proporción de NULOS en cada una de las columnas del conjunto de datos:')
    print(round((df.isnull().sum()/len(df))*100, 2).sort_values(ascending= False))
    print('###################################################################################')
    print(f'3.1.2. Número de DUPLICADOS totales: {df.duplicated().sum()}')
    print('###################################################################################')
    if len(columnas) > 0:
        print(f'3.1.2. Número de DUPLICADOS parciales según las columnas {columnas}: {df.duplicated(subset=columnas).sum()}')
        print('###################################################################################')
    df_numericas = df.select_dtypes(include = 'number')
    columnas_numericas = list(df_numericas.columns)
    if len(columnas_numericas) > 0:
        print('3.1.3. Columnas numéricas con OUTLIERS')
        for var in columnas_numericas:
            Q1 = df[var].quantile(0.25)
            Q3 = df[var].quantile(0.75)
            limite_inferior = Q1 - 1.5 * (Q3 - Q1)
            limite_superior = Q3 + 1.5 * (Q3 - Q1)
            outliers = df[(df[var] < limite_inferior) | (df[var] > limite_superior)]
            print(f'Número de outliers en la columna "{var}": {outliers.shape[0]}')
        print('###################################################################################')

# FUNCIÓN PARA DETECTAR OUTLIERS

def deteccion_outliers (df, columna):
    # Calcular Q1, Q3 e IQR
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1

    # Definir límites inferior y superior para detectar outliers
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    print(f"Los valores atípicos se definen como aquellos que caen fuera del siguiente rango:")
    print(f"\t - Límite inferior (considerado extremadamente bajo): {limite_inferior:.2f}")
    print(f"\t - Límite superior (considerado extremadamente alto): {limite_superior:.2f}")

    # Identificar los outliers
    outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]

    print(f'Número de outliers en la columna "{columna}": {outliers.shape[0]}')
    return outliers

# FUNCIÓN PARA PROCESAR FECHAS

def procesar_fecha(fecha):
  '''
    * Separados por "-":
      - Patrón 1: 04-01-2020
      - Patrón 2: 2020-01-10
      - Patrón 3: 01-14-20

    * Separados por "/":
      - Patrón 4: 11/01/2020
      - Patrón 5: 02/03/20
  '''

  # Separador '-'

  # %d-%m-%y'
  patron1 = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{2})$'
  # dia: (0[1-9]|[12][0-9]|3[01])
  # mes: (0[1-9]|1[0-2])
  # año: (\d{2})

  #'%d-%m-%Y'
  patron2 = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$'

  #'%m-%d-%y'
  patron3 = r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{2})$'

  #'%m-%d-%Y'
  patron4 = r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$'

  #'%Y-%m-%d'
  patron5 = r'^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'

  # Separador '/'

  #'%d/%m/%y'
  patron6 = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$'

  #'%m/%d/%y'
  patron7 = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})$'

  #'%m/%d/%Y'
  patron8 = r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$'

  #'%Y/%m/%d'
  patron9 = r'^(\d{4})/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$'

  #'%Y/%m/%d'
  patron10 = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$'

  # 12/5/2021	
  #'%Y/%m/%d'
  patron11 = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{4})$'

  # Comprueba si la fecha cumple con el patrón
  if pd.notnull(fecha) and re.fullmatch(patron1, fecha):
    # Parsea la fecha al formato deseado y devuelve en formato "aaaa-mm-dd"
    return pd.to_datetime(fecha, format='%d-%m-%y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron2, fecha):
    return pd.to_datetime(fecha, format='%d-%m-%Y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron3, fecha):
    return pd.to_datetime(fecha, format='%m-%d-%y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron4, fecha):
    return pd.to_datetime(fecha, format='%m-%d-%Y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron5, fecha):
    return pd.to_datetime(fecha, format='%Y-%m-%d').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron6, fecha):
    return pd.to_datetime(fecha, format='%d/%m/%y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron7, fecha):
      return pd.to_datetime(fecha, format='%m/%d/%y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron8, fecha):
      return pd.to_datetime(fecha, format='%m/%d/%Y').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron9, fecha):
      return pd.to_datetime(fecha, format='%Y/%m/%d').strftime('%Y-%m-%d')

  elif pd.notnull(fecha) and re.fullmatch(patron10, fecha):
      return pd.to_datetime(fecha, format='%d/%m/%Y').strftime('%Y-%m-%d')
  
  # 12/5/2021
  elif pd.notnull(fecha) and re.fullmatch(patron11, fecha):
      return pd.to_datetime(fecha, format='%m/%d/%Y').strftime('%Y-%m-%d')

  else:
      # Devuelve la fecha original si no cumple con el patrón o es NaN
      return pd.NaT  # Retorna Not a Time para fechas que no coinciden con ningún formato
  
# FUNCIÓN PARA MAYÚSCULAS

def palabra_mayuscula(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.capitalize()
    return df


  
