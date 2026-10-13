from src.data import generate_headcount_history
from src.forecast import forecast_headcount

def test_forecast_length():
    df = generate_headcount_history(12)
    f = forecast_headcount(df, 6)
    assert len(f) == 6
