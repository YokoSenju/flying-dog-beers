import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
from scipy.integrate import odeint

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='lightblue'
color2='darkgreen'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='MEU PAU VOANDO PELO UNIVERSO'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
N=1500
I0=2.0
beta = 0.296
gamma = 0.07
mu = 0.007

def f(x,t):
	S = x[0]
	I = x[1]
	R = x[2]
	M = x[3]
	dSdt = -beta*I*S/N
	dIdt = beta*I*S/N -gamma*I - mu*I
	dRdt = gamma*I
	dMdt = mu*I
	return [dSdt,dIdt,dRdt,dMdt]
t = np.linspace(0, 60)
corona0 = [N-I0,I0,0,0]
corona = odeint(f,corona0,t)
ft = corona[:,1]
graph = go.Scatter(
	x=t,
	y=ft
)

dat = [graph]

beer_fig = go.Figure(data=dat)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('MEU PAU', href=githublink),
    html.Br(),
    html.A('VOANDO', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
