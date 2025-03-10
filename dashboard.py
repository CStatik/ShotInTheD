import dash
import dash_core_components as dcc
import dash_html_components as html
import psutil

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Key Search Monitoring"),
    dcc.Graph(id="cpu-usage"),
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=5000)
