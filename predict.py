import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).with_name("hotel_cancellation_pipeline.joblib")
MODEL_FEATURES = ['hotel', 'lead_time', 'arrival_date_year', 'arrival_date_month', 'arrival_date_week_number', 'arrival_date_day_of_month', 'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children', 'babies', 'meal', 'country', 'market_segment', 'distribution_channel', 'is_repeated_guest', 'previous_cancellations', 'previous_bookings_not_canceled', 'reserved_room_type', 'agent', 'company', 'customer_type', 'total_nights', 'total_guests', 'has_children', 'arrival_month', 'arrival_dow', 'arrival_is_weekend', 'arrival_month_sin', 'arrival_month_cos', 'lead_time_band', 'prev_cancel_ratio']
CANCELLATION_THRESHOLD = 0.5
MONTHS = {name: index for index, name in enumerate(
    ["January", "February", "March", "April", "May", "June",
     "July", "August", "September", "October", "November", "December"],
    start=1,
)}


def prepare_features(raw_data):
    data = raw_data.copy()
    if "arrival_date" not in data.columns:
        data["arrival_date"] = pd.to_datetime(dict(
            year=data["arrival_date_year"],
            month=data["arrival_date_month"].map(MONTHS),
            day=data["arrival_date_day_of_month"],
        ))
    else:
        data["arrival_date"] = pd.to_datetime(data["arrival_date"])

    data["total_nights"] = data["stays_in_weekend_nights"] + data["stays_in_week_nights"]
    data["total_guests"] = data["adults"] + data["children"].fillna(0) + data["babies"]
    data["has_children"] = (
        (data["children"].fillna(0) + data["babies"]) > 0
    ).astype(int)
    data["arrival_month"] = data["arrival_date"].dt.month
    data["arrival_dow"] = data["arrival_date"].dt.day_of_week
    data["arrival_is_weekend"] = data["arrival_dow"].isin([5, 6]).astype(int)
    data["arrival_month_sin"] = np.sin(2 * np.pi * data["arrival_month"] / 12)
    data["arrival_month_cos"] = np.cos(2 * np.pi * data["arrival_month"] / 12)
    data["lead_time_band"] = pd.cut(
        data["lead_time"],
        bins=[-1, 7, 30, 90, 180, 365, np.inf],
        labels=["0-7", "8-30", "31-90", "91-180", "181-365", "366+"],
    ).astype("object")
    prior_bookings = data["previous_cancellations"] + data["previous_bookings_not_canceled"]
    data["prev_cancel_ratio"] = data["previous_cancellations"].div(
        prior_bookings.where(prior_bookings > 0)
    ).fillna(0)
    return data


def predict_reservations(raw_data, model_path=MODEL_PATH):
    model = joblib.load(model_path)
    features = prepare_features(raw_data)
    probabilities = model.predict_proba(features[MODEL_FEATURES])[:, 1]
    result = raw_data.copy()
    result["cancellation_probability"] = probabilities
    result["predicted_cancellation"] = (
        probabilities >= CANCELLATION_THRESHOLD
    ).astype(int)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python predict.py reservations.csv")
    predictions = predict_reservations(pd.read_csv(sys.argv[1]))
    print(predictions.to_string(index=False))
