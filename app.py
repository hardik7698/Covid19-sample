from dash import Dash
import dash
import pandas as pd
import dash_bootstrap_components as dbc
from layout import layout
from dash.dependencies import Input,Output,State
from movie import x
import dash_bootstrap_components as dbc
import plotly.express as px

app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.title="covid report"
# app.
app.layout=layout

d1={}
@app.callback(
Output("flag","src"),
[Input("country","value")]  
)
def op(ccode):
    if ccode is None:
        dash.exceptions.PreventUpdate
    return f"https://www.countryflags.io/{ccode}/shiny/64.png"

@app.callback(
Output("Symb","children"),
[Input("country","value")]  
)
def op(sym):
    if sym is None:
        name=""
    else:
        name=str(x['administrative_area_level_1'][x['iso_alpha_2']==sym].unique()[0])
    return f"{name}"


@app.callback(
Output("map","figure"),
[Input("country","value")]  
)
def op(sym):
    df11=pd.DataFrame(x.query(f'iso_alpha_2=="{sym}"')[['confirmed','latitude','longitude','tests']])
    # print(df11)
    fig = px.scatter_mapbox(df11.iloc[-1:,:], lat="latitude", lon="longitude", hover_name="tests",
    hover_data=["tests", "confirmed"],color_discrete_sequence=["red"], zoom=3,size="confirmed", height=511)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_traces(hovertemplate='<b>confirmed=%{customdata[1]}</b><br><br>tests=%{customdata[0]}<extra></extra>')
    # pd.to_csv(fig)
   
    return fig

@app.callback(
Output("desc","children"),
[Input("country","value")]  
)
def popu(popu):
    if popu is None:
        popu1=""
        curr=""
    else:
        popu1=str(x['population'][x['iso_alpha_2']==popu].unique()[0])
        curr1=str(x['currency'][x['iso_alpha_2']==popu].unique()[0])
        d1['Population']=[popu1]
        d1['currency']=[curr1]
        df=pd.DataFrame(d1)
        return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

@app.callback(
Output("line","figure"),
[Input("country","value")]  
)
def popu(popu):
    dx=x[x['iso_alpha_2']==popu]
    # dx.fillna("NONE")
    # print(dx)
    fig1=px.line(dx, x="date", y=dx.columns[5:7], title='Confirmed cases')  
    fig1.update_layout(
    plot_bgcolor="white"
    )
    fig1.update_traces(hovertemplate= '<br>date=%{x}<br>value=%{y}<extra></extra>')

    # print(fig1)
    return fig1 

if __name__ == '__main__':
    app.run_server(debug=True)
