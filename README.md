# Obligatorio de Inteligencia Artificial

Proyecto académico de predicción de cancelaciones hoteleras. El notebook [obligatorio_hotel_cancelaciones.ipynb](./obligatorio_hotel_cancelaciones.ipynb) contiene el código y breves indicaciones en español. La explicación metodológica completa, las decisiones, los resultados y las limitaciones están en el informe Word actualizado, cuya versión fuente se mantiene en Google Drive.

## Archivos

- `hotel_bookings.csv`: datos del proyecto.
- `obligatorio_hotel_cancelaciones.ipynb`: código reproducible con indicaciones breves en español.
- `requirements.txt`: versiones fijadas de las dependencias Python.
- `Obligatorio Inteligencia Artificial.docx`: informe con la explicación completa y la ortografía revisada.
- `Obligatorio Inteligencia Artificial.pdf`: exportación anterior; volver a generarla desde el DOCX antes de usarla como entrega.
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

**Ejecutar todo** vuelve a crear `test_holdout.csv` en el entorno de Colab y ejecuta la exploración, la validación temporal, el ajuste y la interpretabilidad; el análisis completo puede tardar varios minutos. La celda final mantiene `RUN_FINAL_TEST_EVALUATION = False`, por lo que no lee ni reevalúa el conjunto de prueba. No cambies el indicador durante la presentación ni uses ese conjunto para seleccionar modelos, variables o umbrales. Las celdas que generan un DOCX son opcionales y continúan sin error si el archivo fuente no está cargado en Colab.

## Flujo de ramas

Trabaja en una rama propia y abre un pull request hacia `main`. No hagas commits directamente en `main`; revisa que el pull request no incluya `test_holdout.csv` ni artefactos generados. El repositorio aún necesita una regla de protección de rama en GitHub para hacer cumplir este flujo.

## Datos y limitaciones

El dataset Hotel Booking Demand fue publicado por Antonio, Almeida y Nunes (2019), *Data in Brief*, 22, 41–49, https://doi.org/10.1016/j.dib.2018.11.126. Esta copia fue distribuida en [Kaggle](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/data) bajo licencia Attribution 4.0 International. Los datos corresponden a dos hoteles y no garantizan generalización a otros establecimientos o períodos.
