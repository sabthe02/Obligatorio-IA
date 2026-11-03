# Obligatorio de Inteligencia Artificial

Proyecto de predicción de cancelaciones hoteleras. El análisis, la partición temporal, el entrenamiento y la evaluación están documentados en [obligatorio_hotel_cancelaciones.ipynb](./obligatorio_hotel_cancelaciones.ipynb).

## Archivos

- `hotel_bookings.csv`: datos del proyecto.
- `Obligatorio Inteligencia Artificial.docx`: informe del equipo.
- `requirements.txt`: versiones de las dependencias Python.

## Ejecución

El entorno previsto es Google Colab. También se puede abrir el notebook desde VS Code con la extensión Jupyter:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En Colab, conservar `hotel_bookings.csv` junto al notebook o usar el enlace del badge al inicio del archivo.

La celda de partición genera `test_holdout.csv` localmente; el archivo está excluido de Git. La evaluación final permanece desactivada hasta acordar el umbral operativo. No se debe usar el holdout para seleccionar modelos, variables ni umbrales.

## Datos y limitaciones

El dataset Hotel Booking Demand fue publicado por Antonio, Almeida y Nunes (2019), *Data in Brief*, 22, 41–49, https://doi.org/10.1016/j.dib.2018.11.126. Esta copia fue distribuida en [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data) bajo licencia Attribution 4.0 International. Los datos corresponden a dos hoteles y no garantizan generalización a otros establecimientos o períodos.
