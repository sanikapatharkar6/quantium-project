import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read data
df = pd.read_csv("formatted_output.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales",
        "region": "Region"
    }
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualiser"),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)