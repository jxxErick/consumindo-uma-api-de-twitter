import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from src.services import get_trends

app_dash = dash.Dash(__name__)

app_dash.layout = html.Div(children=[
    html.H1(children='Twitter Trends Dashboard'),
    
    dcc.Graph(
        id='trends-graph',
        figure={
            'data': [
                {'x': [trend['name'] for trend in get_trends()], 'y': [1] * len(get_trends()), 'type': 'bar', 'name': 'Trends'},
            ],
            'layout': {
                'title': 'Twitter Trends',
            }
        }
    )
])

if __name__ == '__main__':
    app_dash.run_server(debug=True)
