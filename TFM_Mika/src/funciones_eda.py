import plotly.express as px

# BOXPLOT

def graficar_boxplot_px(df, variable_analisis):
    # Crear el boxplot usando Plotly Express
    fig = px.box(df, y=variable_analisis)

    # Actualizar títulos del gráfico
    fig.update_layout(title=f'Boxplot: {variable_analisis}',
                      yaxis_title='Frecuencia')

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()

def graficar_boxplot_bivariable_px (df, variable_analisis, variable_categorica):
    # Crear el boxplot usando Plotly Express
    fig = px.box(df, x=variable_categorica, y=variable_analisis, color=variable_categorica) 

    # Actualizar títulos del gráfico
    fig.update_layout(title=f'Boxplot de {variable_analisis} por {variable_categorica}',
                      xaxis_title=variable_categorica,
                      yaxis_title=variable_analisis)

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()

# HISTOGRAMA

def graficar_histograma_px (df, variable_analisis):
    fig = px.histogram(df, x=variable_analisis, nbins=20,
                       title=f'Distribución de: {variable_analisis}')
    
    # Calcular media y mediana
    mean_val = df[variable_analisis].mean()
    median_val = df[variable_analisis].median()

    # Añadir línea vertical para la media
    fig.add_vline(x=mean_val, line_dash="dash", line_color="red",
                  annotation_text=f"Media: {mean_val:.2f}", annotation_position="top right")
    
    # Añadir línea vertical para la mediana
    fig.add_vline(x=median_val, line_dash="dot", line_color="green",
                  annotation_text=f"Mediana: {median_val:.2f}", annotation_position="top left")
    
    fig.update_layout(xaxis_title=variable_analisis, yaxis_title='Frecuencia')
    fig.show()

# DIAGRAMA DE BARRAS

def graficar_barras_px (df, variable_analisis):
    # Contar la frecuencia de la variable de análisis
    volumen = df[variable_analisis].value_counts().reset_index()
    volumen.columns = [variable_analisis, 'Volúmen']

    # Crear el gráfico de barras
    fig = px.bar(volumen, x=variable_analisis, y='Volúmen', text='Volúmen')
    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(title_text=f'Gráfico de barras: {variable_analisis}',
                      xaxis_title=variable_analisis,
                      yaxis_title='Volúmen',
                      xaxis={'categoryorder':'total descending'})

    # Actualizar el fondo del gráfico a blanco
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    fig.show()

# GRÁFICO DE TARTA

def graficar_pie_chart(df, variable_analisis):
  df_ = df[variable_analisis].value_counts().reset_index()
  df_.columns = [
      variable_analisis,
      'Volúmen'
  ]

  fig = px.pie(
      df_,
      names=variable_analisis,
      values='Volúmen',
      title=variable_analisis,
      width=800,
      height=500
  )
  fig.show()

# SCATTERPLOT

def graficar_correlacion(df, variable_x, variable_y):
    # Crear el gráfico de dispersión usando Plotly Express para visualizar la correlación
    fig = px.scatter(df, x=variable_x, y=variable_y,
                     trendline='ols',  # Añade una línea de regresión
                     labels={variable_x: variable_x, variable_y: variable_y},
                     title=f'Correlación entre {variable_x} y {variable_y}')

    # Actualizar el fondo del gráfico a blanco y ajustar la cuadrícula
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',
        'xaxis': {'showgrid': True, 'gridcolor': 'lightgrey'},
        'yaxis': {'showgrid': True, 'gridcolor': 'lightgrey'}
    })

    # Mostrar el gráfico
    fig.show()

# FUNCIÓN PARA GRÁFICA ENTRE DATOS CATEGÓRICOS

def grafica_categorica(df, columna_categorica, target='y'):
    import plotly.express as px

    fig = px.histogram(
        df,
        x=columna_categorica,
        color=target,
        barmode='group',
        title=f'Distribución de {target} por {columna_categorica}'
    )
    fig.show()

