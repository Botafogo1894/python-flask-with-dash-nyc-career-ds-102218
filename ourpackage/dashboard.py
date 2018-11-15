import dash_core_components as dcc
import dash_html_components as html
from ourpackage import app
from ourpackage.uber_data import data



# uncomment and write the code for our Dash app below:

app.layout = html.Div(children=[
             html.H1("Check it out! This app has Flask AND Dash"),
             html.Div([
        html.P('Dash converts Python classes into HTML'),
            html.Div([
                dcc.Graph( id='my squish',
                    figure= dict(data = [{'x': [1,2,3], 'y': [5,6,7]}]))
                ])
            ])
])
