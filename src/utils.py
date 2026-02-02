# 1-Checkear información


def check_df(df, tipo="full", sample_n=5):
    """
    Inspección rápida de un DataFrame.

    Parámetros
    ----------
    df : pandas.DataFrame
    tipo : str
        'simple' o 'full'
    sample_n : int
        Número de filas para la muestra aleatoria
    """

    def separador():
        print("\n" + "#" * 90 + "\n")

    # Dimensiones
    print("¿Cuántas filas y columnas hay en el conjunto de datos?")
    filas, columnas = df.shape
    print(f"\tHay {filas:,} filas y {columnas:,} columnas.")
    separador()

    # Head
    n_head = 2 if tipo == "simple" else 5
    print(f"¿Cuáles son las primeras {n_head} filas del conjunto de datos?")
    display(df.head(n_head))

    if tipo == "simple":
        return

    separador()

    # Tail
    print("¿Cuáles son las últimas cinco filas del conjunto de datos?")
    display(df.tail())
    separador()

    # Sample
    print("¿Cómo puedes obtener una muestra aleatoria de filas del conjunto de datos?")
    display(df.sample(n=min(sample_n, len(df))))
    separador()

    # Tipos de datos
    print("¿Cuál es el tipo de datos de cada columna?")
    display(df.dtypes)
    separador()

    print("¿Cuántas columnas hay de cada tipo de datos?")
    display(df.dtypes.value_counts())
    separador()

    # Variables numéricas y categóricas
    df_numericas = df.select_dtypes(include="number")
    df_categoricas = df.select_dtypes(exclude="number")

    print("Variables numéricas:")
    print(list(df_numericas.columns))
    separador()

    print("Variables categóricas:")
    print(list(df_categoricas.columns))
    separador()

    # Valores únicos
    print("¿Cuántos valores únicos tiene cada columna?")
    display(df.nunique())
    separador()

    # Estadísticas
    if not df_numericas.empty:
        print("Estadísticas descriptivas (numéricas):")
        display(df_numericas.describe())
        separador()

    if not df_categoricas.empty:
        print("Estadísticas descriptivas (categóricas):")
        display(df_categoricas.describe())
        separador()

    return df_numericas, df_categoricas


########################################################################################################################################################################################


# 2-Identificar problemas
def identificacion_valores_problem(df, columnas=[]):
    print(
        "###################################################################################"
    )
    print(
        "3.1.1. Proporción de NULOS en cada una de las columnas del conjunto de datos:"
    )
    print(round((df.isnull().sum() / len(df)) * 100, 2).sort_values(ascending=False))
    print(
        "###################################################################################"
    )
    print(f"3.1.2. Número de DUPLICADOS totales: {df.duplicated().sum()}")
    print(
        "###################################################################################"
    )
    if len(columnas) > 0:
        print(
            f"3.1.2. Número de DUPLICADOS parciales según las columnas {columnas}: {df.duplicated(subset=columnas).sum()}"
        )
        print(
            "###################################################################################"
        )
    df_numericas = df.select_dtypes(include="number")
    columnas_numericas = list(df_numericas.columns)
    if len(columnas_numericas) > 0:
        print("3.1.3. Columnas numéricas con OUTLIERS")
        for var in columnas_numericas:
            Q1 = df[var].quantile(0.25)
            Q3 = df[var].quantile(0.75)
            limite_inferior = Q1 - 1.5 * (Q3 - Q1)
            limite_superior = Q3 + 1.5 * (Q3 - Q1)
            outliers = df[(df[var] < limite_inferior) | (df[var] > limite_superior)]
            print(f'Número de outliers en la columna "{var}": {outliers.shape[0]}')
        print(
            "###################################################################################"
        )


########################################################################################################################################################################################


# 3-Procesar fecha
def procesar_fecha(fecha):
    """
    * Separados por "-":
      - Patrón 1: 04-01-2020
      - Patrón 2: 2020-01-10
      - Patrón 3: 01-14-20

    * Separados por "/":
      - Patrón 4: 11/01/2020
      - Patrón 5: 02/03/20
    """

    # Separador '-'

    # %d-%m-%y'
    patron1 = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{2})$"
    # dia: (0[1-9]|[12][0-9]|3[01])
    # mes: (0[1-9]|1[0-2])
    # año: (\d{2})

    #'%d-%m-%Y'
    patron2 = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$"

    #'%m-%d-%y'
    patron3 = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{2})$"

    #'%m-%d-%Y'
    patron4 = r"^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$"

    #'%Y-%m-%d'
    patron5 = r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

    # Separador '/'

    #'%d/%m/%y'
    patron6 = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{2})$"

    #'%m/%d/%y'
    patron7 = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{2})$"

    #'%m/%d/%Y'
    patron8 = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$"

    #'%Y/%m/%d'
    patron9 = r"^(\d{4})/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$"

    #'%Y/%m/%d'
    patron10 = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(\d{4})$"

    # 12/5/2021
    #'%Y/%m/%d'
    patron11 = r"^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{4})$"

    # Comprueba si la fecha cumple con el patrón
    if pd.notnull(fecha) and re.fullmatch(patron1, fecha):
        # Parsea la fecha al formato deseado y devuelve en formato "aaaa-mm-dd"
        return pd.to_datetime(fecha, format="%d-%m-%y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron2, fecha):
        return pd.to_datetime(fecha, format="%d-%m-%Y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron3, fecha):
        return pd.to_datetime(fecha, format="%m-%d-%y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron4, fecha):
        return pd.to_datetime(fecha, format="%m-%d-%Y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron5, fecha):
        return pd.to_datetime(fecha, format="%Y-%m-%d").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron6, fecha):
        return pd.to_datetime(fecha, format="%d/%m/%y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron7, fecha):
        return pd.to_datetime(fecha, format="%m/%d/%y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron8, fecha):
        return pd.to_datetime(fecha, format="%m/%d/%Y").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron9, fecha):
        return pd.to_datetime(fecha, format="%Y/%m/%d").strftime("%Y-%m-%d")

    elif pd.notnull(fecha) and re.fullmatch(patron10, fecha):
        return pd.to_datetime(fecha, format="%d/%m/%Y").strftime("%Y-%m-%d")

    # 12/5/2021
    elif pd.notnull(fecha) and re.fullmatch(patron11, fecha):
        return pd.to_datetime(fecha, format="%m/%d/%Y").strftime("%Y-%m-%d")

    else:
        # Devuelve la fecha original si no cumple con el patrón o es NaN
        return (
            pd.NaT
        )  # Retorna Not a Time para fechas que no coinciden con ningún formato


######################################################################################################################
# 5 Crear un boxplot_px variable numerico


def graficar_boxplot_px(df, variable_analisis):
    # Crear el boxplot usando Plotly Express
    fig = px.box(df, y=variable_analisis)

    # Actualizar títulos del gráfico
    fig.update_layout(title=f"Boxplot: {variable_analisis}", yaxis_title="Frecuencia")

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout(
        {
            "plot_bgcolor": "rgba(255, 255, 255, 1)",
            "xaxis": {"showgrid": True, "gridcolor": "lightgrey"},
            "yaxis": {"showgrid": True, "gridcolor": "lightgrey"},
        }
    )

    # Mostrar el gráfico
    fig.show()


###############################################################################################################


# 6.LIMITES OUTLIERS
def limites_outliers(df, nombre_columna):

    columna = df[nombre_columna]

    Q1 = columna.quantile(0.25)
    Q3 = columna.quantile(0.75)
    IQR = Q3 - Q1
    print("Valor del segundo cuartil (25%): {:.2f}".format(Q1))
    print("Valor del tercer cuartil (75%): {:.2f}".format(Q3))
    print("Valor del rango intercuartil (IQR): {:.2f}".format(IQR))

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    print(
        f"Los valores atípicos se definen como aquellos que caen fuera del siguiente rango:"
    )
    print(
        f"\t - Límite inferior (considerado extremadamente bajo): {limite_inferior:.2f}"
    )
    print(
        f"\t - Límite superior (considerado extremadamente alto): {limite_superior:.2f}"
    )

    return limite_inferior, limite_superior


###################

def jobType(valor):
    no_job = ['student','retired','unemployed']
    office_job = ['services','admin.','management']
    physical_job = ['housemaid','blue-collar','technician']
    self_employed = ['entrepreneur','self-employed']

    if valor in no_job:
        return 'No Job or Retired'
    elif valor in office_job:
        return 'Office Job'
    elif valor in physical_job:
        return "Physical Job"
    elif valor in self_employed:
        return "Self-Employed"
    else:
        return 'Unknown' 
    
##########

def educationType(valor):
    basic_education = ['basic.4y','basic.6y','basic.9y']
    high_school = ['high.school']
    higher_education = ['university.degree','professional.course']

    if valor in basic_education:
        return 'Basic Education (Yr 4-9)'
    elif valor in high_school:
        return 'High School'
    elif valor in higher_education:
        return "University or Professional Program"
    else:
        return 'Unknown or Illiterate' 