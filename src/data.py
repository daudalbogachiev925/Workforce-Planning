import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_headcount_history(months=24, seed=42):
    np.random.seed(seed)
    dates = [datetime(2023, 1, 1) + timedelta(days=30*i) for i in range(months)]
    base = 500
    headcount = []
    for i in range(months):
        base = base * (1 + np.random.normal(0.02, 0.01))
        headcount.append(int(base))
    return pd.DataFrame({"date": dates, "headcount": headcount})
