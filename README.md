FINTECH – Data Analytics & Marketing Campaign Optimization

Trabajo Final de Máster enfocado en el análisis de campañas de marketing de una empresa Fintech con el objetivo de identificar los factores que influyen en la contratación de depósitos a plazo fijo.

🔗 Repositorio:
https://github.com/diegodelarubia/Trabajo_Final_Master-TFM-/tree/master

A través de técnicas de análisis exploratorio de datos (EDA), visualización de datos y modelado predictivo, se busca entender el comportamiento de los clientes y mejorar la eficiencia de las campañas de marketing.

Objetivo del proyecto

El objetivo principal del proyecto es:

Aumentar la tasa de conversión en la contratación de depósitos mediante el análisis de datos de campañas de marketing.

Para ello se han desarrollado:

Análisis exploratorio de los datos
Visualización de patrones y tendencias
Segmentación de clientes
Identificación de variables clave en la conversión
Desarrollo de un modelo predictivo de conversión
Definición de KPIs estratégicos para negocio
Dataset

El proyecto utiliza el dataset Bank Marketing Dataset, que recoge información sobre campañas de marketing realizadas por una entidad financiera.

Incluye variables como:

Datos demográficos del cliente
Información socioeconómica
Características del contacto
Resultado de la campaña

Variable objetivo:
y → contratación del depósito (yes / no)

Estructura del proyecto
TFM_FINTECH
│
├── data
│   └── bank-additional-full.csv
│
├── notebooks
│   └── TFM_analysis.ipynb
│
├── src
│   ├── utils_analysis.py
│   └── utils_visualization.py
│
├── requirements.txt
│
└── README.md
Tecnologías utilizadas
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
Scikit-learn
Instalación

Clonar el repositorio:

git clone https://github.com/diegodelarubia/Trabajo_Final_Master-TFM-.git
cd Trabajo_Final_Master-TFM-

Instalar dependencias:

pip install -r requirements.txt
Ejecución del proyecto

Abrir el notebook principal:

notebooks/TFM_analysis.ipynb

Ejecutar las celdas en orden para reproducir el análisis completo.

Modelo predictivo (Machine Learning)

Como parte del proyecto, se ha desarrollado un modelo de Machine Learning con el objetivo de predecir la probabilidad de conversión de un cliente y apoyar la toma de decisiones en campañas de marketing.

Enfoque del modelado
Preparación y limpieza de datos
Codificación de variables categóricas
Selección de variables relevantes
División del dataset en entrenamiento y test
Entrenamiento de modelos de clasificación
Modelos evaluados
Regresión Logística
Árboles de decisión
Random Forest
Métricas de evaluación
Precision
Recall
F1-score
Matriz de confusión
Principales resultados
Identificación de clientes con mayor probabilidad de conversión
Validación de variables clave detectadas en el EDA
Utilidad del modelo para priorización de contactos
Aplicación en negocio
Priorización de clientes con mayor probabilidad de conversión
Optimización de recursos comerciales
Mejora de la eficiencia de campañas
Apoyo a estrategias de segmentación y retargeting
Resultados del proyecto

El análisis permite:

Identificar los segmentos de clientes con mayor probabilidad de conversión
Entender qué variables influyen en la contratación del depósito
Optimizar la asignación de recursos en campañas de marketing
Definir KPIs estratégicos para mejorar la eficiencia de negocio
Autores

Proyecto desarrollado por:

Diego González de la Rubia
María Egea Miró
Leonardo Betancourt
David Lombardini
Miguel Retegui

Máster en Data Visualization & Analytics
