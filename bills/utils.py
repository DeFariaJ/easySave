import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Gauge chart


def gauge_chart(value):
    fig3 = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        delta={'reference': 1260, "decreasing": {
            "color": "green"}},
        value=value,
        domain={'x': [0.1, 1], 'y': [0.2, 0.9]},
        title={'text': "Bills"},
        gauge={
            'axis': {
                'range': [None, 1500],
            },
            "shape": "bullet",
            "bar": {"color": "darkblue"},
            'bgcolor': "lavender",
            'borderwidth': 3,
            'bordercolor': "black",
            'threshold': {
                'value': 1260,
                'line': {'color': "red", "width": 4}
            }
        }))
    return fig3
