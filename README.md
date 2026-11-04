# Obligatorio de Inteligencia Artificial

Proyecto académico de predicción de cancelaciones hoteleras. El análisis, la partición temporal, el entrenamiento y la evaluación están documentados en [obligatorio_hotel_cancelaciones.ipynb](./obligatorio_hotel_cancelaciones.ipynb). El informe actualizado del equipo se mantiene en Google Drive.

## Archivos

- `hotel_bookings.csv`: datos del proyecto.
- `obligatorio_hotel_cancelaciones.ipynb`: análisis y evaluación.
- `requirements.txt`: versiones fijadas de las dependencias Python.
- `hotel_cancellation_pipeline.joblib` y `predict.py`, cuando estén disponibles: pipeline calibrado y script de predicción.
- Informe final en Google Drive y sus exportaciones DOCX/PDF.

## Ejecución

En Google Colab, conserva `hotel_bookings.csv` junto al notebook o usa el enlace de descarga configurado en la celda de carga. El badge del notebook abre la versión de la rama `Sabine`.

Para ejecución local en Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

La partición crea `test_holdout.csv` localmente. Está excluido de Git: no lo fuerces ni lo agregues al repositorio. El holdout ya se evaluó una sola vez; la celda de evaluación está protegida y desactivada. No lo vuelvas a abrir para seleccionar modelos, variables o umbrales.

## Flujo de ramas

Trabaja en una rama propia y abre un pull request hacia `main`. No hagas commits directamente en `main`; revisa que el pull request no incluya `test_holdout.csv` ni artefactos generados. El repositorio aún necesita una regla de protección de rama en GitHub para hacer cumplir este flujo.

## Datos y limitaciones

El dataset Hotel Booking Demand fue publicado por Antonio, Almeida y Nunes (2019), *Data in Brief*, 22, 41–49, https://doi.org/10.1016/j.dib.2018.11.126. Esta copia fue distribuida en [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data) bajo licencia Attribution 4.0 International. Los datos corresponden a dos hoteles y no garantizan generalización a otros establecimientos o períodos.
