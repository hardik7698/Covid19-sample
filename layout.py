import dash_core_components as dcc
from dash import Dash
import dash_html_components as html
from dash.dependencies import Input,Output,State
import dash_bootstrap_components as dbc
from dash import Dash
from movie import countries,countriesid
from movie import x
app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


layout=html.Div([
    dbc.Row([
        dbc.Col(),
        dbc.Col(
        dcc.Dropdown(id="country",
        placeholder="Country",
        value="IN",
        options=[{'label':i,'value': j} for i,j in zip(countries,countriesid)],
      
    ),style={'margin':'1%'}
    ),
    dbc.Col()]),
    dbc.Row([
        
        dbc.Col([
            dbc.Card(
            [
            dbc.CardHeader(id='Symb',style={'text-align':'center','font-size':'25px'}),
            dbc.CardImg(id="flag",top=True),
            dbc.CardBody(
            [
                
                html.P(
                    id='desc',
                    className="card-text",style={'text-align':'center','font-size':'18px'}
                ),
                
            ]
        ),
            ],style={'width':'18rem'})
        
        ]
    ),dbc.Col(dcc.Graph(id='map')),
    dbc.Col(dcc.Graph(id="line")),

    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id="com selected"))
    ])
],style={'margin':"1%"}
)



