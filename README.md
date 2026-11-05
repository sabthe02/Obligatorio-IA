# Obligatorio de Inteligencia Artificial

Proyecto académico de predicción de cancelaciones hoteleras. El análisis, la partición temporal, el entrenamiento y la evaluación están documentados en [obligatorio_hotel_cancelaciones.ipynb](./obligatorio_hotel_cancelaciones.ipynb). El informe actualizado del equipo se mantiene en Google Drive.

## Archivos

- `hotel_bookings.csv`: datos del proyecto.
- `obligatorio_hotel_cancelaciones.ipynb`: análisis y evaluación.
- `requirements.txt`: versiones fijadas de las dependencias Python.
- `Obligatorio Inteligencia Artificial.docx` y `Obligatorio Inteligencia Artificial.pdf`: informe actualizado, sincronizado con el Google Doc.
- `hotel_cancellation_pipeline.joblib` y `predict.py`, cuando estén disponibles: pipeline calibrado y script de predicción.
- `OLD/`: versiones anteriores archivadas; no son los entregables vigentes.

## Ejecución

En Google Colab, conserva `hotel_bookings.csv` junto al notebook o usa el enlace de descarga configurado en la celda de carga. El badge del notebook abre la versión de la rama `Sabine`.

Para ejecución local en Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

**Run all** vuelve a crear `test_holdout.csv` en el runtime y ejecuta EDA, validación temporal, ajuste e interpretabilidad; el análisis completo puede tardar varios minutos. La celda final mantiene `RUN_FINAL_TEST_EVALUATION = False`, por lo que no lee ni reevalúa ese holdout. No cambies el indicador durante la presentación ni uses el holdout para seleccionar modelos, variables o umbrales. Las celdas que generan un DOCX son opcionales y continúan sin error si el archivo fuente no está cargado en Colab.

## Flujo de ramas

Trabaja en una rama propia y abre un pull request hacia `main`. No hagas commits directamente en `main`; revisa que el pull request no incluya `test_holdout.csv` ni artefactos generados. El repositorio aún necesita una regla de protección de rama en GitHub para hacer cumplir este flujo.

## Datos y limitaciones

El dataset Hotel Booking Demand fue publicado por Antonio, Almeida y Nunes (2019), *Data in Brief*, 22, 41–49, https://doi.org/10.1016/j.dib.2018.11.126. Esta copia fue distribuida en [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data) bajo licencia Attribution 4.0 International. Los datos corresponden a dos hoteles y no garantizan generalización a otros establecimientos o períodos.
