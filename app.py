import streamlit as st
import plotly.express as px
import pandas as pd
from src.data import generate_headcount_history
from src.forecast import forecast_headcount
from src.budget import personnel_budget
from src.scenarios import build_scenarios

st.title("📅 Workforce Planning")

df = generate_headcount_history()
forecast = forecast_headcount(df, 12)
last_date = df["date"].iloc[-1]
future_dates = pd.date_range(last_date, periods=13, freq="ME")[1:]
forecast_df = pd.DataFrame({"date": future_dates, "headcount": forecast})

st.subheader("История и прогноз")
combined = pd.concat([df.assign(type="history"),
                       forecast_df.assign(type="forecast")])
st.plotly_chart(px.line(combined, x="date", y="headcount", color="type"),
                use_container_width=True)

st.subheader("Сценарии на 12 месяцев")
scenarios = build_scenarios(df["headcount"].iloc[-1])
st.json(scenarios)

st.subheader("Бюджет")
sc = st.selectbox("Сценарий", list(scenarios.keys()))
avg_salary = st.number_input("Средняя зарплата", value=150000, step=10000)
b = personnel_budget(scenarios[sc], avg_salary)
st.json({k: f"₽ {v:,.0f}" for k, v in b.items()})
