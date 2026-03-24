# FINTECH – Data Analytics & Marketing Campaign Optimization

Trabajo Final de Máster enfocado en el análisis de campañas de marketing de una empresa Fintech con el objetivo de identificar los factores que influyen en la contratación de depósitos a plazo fijo.

A través de técnicas de **análisis exploratorio de datos (EDA)**, **visualización de datos** y **modelado predictivo**, se busca entender el comportamiento de los clientes y mejorar la eficiencia de las campañas de marketing.

---

# Objetivo del proyecto

El objetivo principal del proyecto es:

**Aumentar la tasa de conversión en la contratación de depósitos mediante el análisis de datos de campañas de marketing.**

Para ello se han desarrollado:

- Análisis exploratorio de los datos
- Visualización de patrones y tendencias
- Segmentación de clientes
- Identificación de variables clave en la conversión
- Desarrollo de un modelo predictivo de conversión
- Definición de KPIs estratégicos para negocio

---

# Dataset

El proyecto utiliza el dataset **Bank Marketing Dataset**, que recoge información sobre campañas de marketing realizadas por una entidad financiera.

Incluye variables como:

- datos demográficos del cliente
- información socioeconómica
- características del contacto
- resultado de la campaña

Variable objetivo:

**y → contratación del depósito (yes / no)**

---

# Estructura del proyecto

```
TFM_FINTECH
│
├── Data
│   └── bank-additional_bank-additional-full.csv
│
├── notebooks_originales
│   ├── analysis_tfm_leoBetancourt.ipynb
│   ├── plantilla_kpis_TFM.ipynb
│   ├── TFM_diego.ipynb
│   └── TFM_leo.ipynb
│
├── TFM_Final
│   ├── functions.py
│   └── main.ipynb
│
├── README.md
└── requirements.txt
```
## Descripción de las carpetas

**Data**  
Contiene el dataset utilizado para el análisis.

**notebooks_originales**  
Incluye los notebooks desarrollados individualmente durante las fases iniciales del proyecto.

**TFM_Final**  
Contiene la versión final unificada del proyecto:
- `main.ipynb` → notebook final con todo el análisis
- `functions.py` → funciones auxiliares utilizadas en el análisis

**requirements.txt**  
Listado de librerías necesarias para ejecutar el proyecto.

**README.md**  
Documentación del repositorio.
---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/usuario/tfm-fintech.git
cd tfm-fintech
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecución del proyecto

Abrir el notebook principal:

```
TFM_Final/main.ipynb
```

Ejecutar las celdas en orden para reproducir el análisis completo.

---

# Resultados del proyecto

El análisis permite:

- identificar los segmentos de clientes con mayor probabilidad de conversión
- entender qué variables influyen en la contratación del depósito
- optimizar la asignación de recursos en campañas de marketing
- definir KPIs estratégicos para mejorar la eficiencia de negocio

---

# Autores

Proyecto desarrollado por:

- Diego González de la Rubia  
- María Egea Miró  
- Leonardo Betancourt  
- David Lombardini  
- Miguel Retegui  

Máster en **Data Visualization & Analytics**
