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
tabtitle='Click COVID-19'
myheading='Click COVID-19'
label1='IBU'
label2='ABV'
githublink='https://github.com/YokoSenju/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
def Corona6(x,t):
	S1 = x[0]
	E1 = x[1]
	I1 = x[2]
	R1 = x[3]
	M1 = x[4]
    
	S2 = x[5]
	E2 = x[6]
	I2 = x[7]
	R2 = x[8]
	M2 = x[9]
    
	S3 = x[10]
	E3 = x[11]
	I3 = x[12]
	R3 = x[13]
	M3 = x[14]
    
	S4 = x[15]
	E4 = x[16]
	I4 = x[17]
	R4 = x[18]
	M4 = x[19]
    
	S5 = x[20]
	E5 = x[21]
	I5 = x[22]
	R5 = x[23]
	M5 = x[24]
    
	S6 = x[25]
	E6 = x[26]
	I6 = x[27]
	R6 = x[28]
	M6 = x[29]
    
	S7 = x[30]
	E7 = x[31]
	I7 = x[32]
	R7 = x[33]
	M7 = x[34]
    
	S8 = x[35]
	E8 = x[36]
	I8 = x[37]
	R8 = x[38]
	M8 = x[39]
    
	N = 23.6e6
	N1 = 0.1367*N
	N2 = 0.1465*N
	N3 = 0.1604*N
	N4 = 0.1621*N
	N5 = 0.1386*N
	N6 = 0.1148*N
	N7 = 0.0790*N
	N8 = 0.0610*N
	N = N1 + N2 + N3 + N4 + N5 + N6 + N7 + N8
		
	#MATRIZ DA POLONIA
	Cij = np.array([
	[3.21, 0.88, 0.96, 1.39, 0.58, 0.80, 0.43, 0.33],
	[0.56, 8.46, 1.05, 0.96, 0.89, 0.46, 0.26, 0.28],
	[0.50, 0.86, 4.92, 1.33, 1.06, 1.08, 0.26, 0.22],
	[0.91, 0.98, 1.65, 2.89, 1.68, 1.20, 0.54, 0.40],
	[0.35, 0.84, 1.24, 1.57, 2.22, 1.19, 0.42, 0.43],
	[0.48, 0.44, 1.24, 1.12, 1.18, 1.80, 0.53, 0.50],
	[0.44, 0.42, 0.52, 0.86, 0.71, 0.91, 0.91, 0.47],
	[0.33, 0.44, 0.41, 0.61, 0.70, 0.81, 0.45, 0.90]
        ])
    
    
	a = 0.071
	c = 1/5.2
	mu = 0.053
	d = 0.00137
	Pb = 0.11
	Pk = Pb*0.08
	Ej = np.array([E1,E2,E3,E4,E5,E6,E7,E8])
	Ij = np.array([I1,I2,I3,I4,I5,I6,I7,I8])
	B1j = sum(Cij[0,:]*Ij)
	k1j = sum(Cij[0,:]*Ej)
    
	B1 = (B1j*Pb/N1)
	c1 = c
	a1 = 10*a
	mu1 = 0
	k1 = k1j*Pk/N1 
	dS1dt = -B1*S1 - k1*S1 + d*R1
	dE1dt = B1*S1 - c1*E1 + k1*S1
	dI1dt = c1*E1 - a1*I1 - mu1*I1
	dR1dt = a1*I1 - d*R1
	dM1dt = mu1*I1
    
    
	B2j = sum(Cij[1,:]*Ij)
	k2j = sum(Cij[1,:]*Ej)
    
	B2 = (B2j*Pb/N2)
	c2 = c
	a2 = (1-0.002)*a
	mu2 = 0.002*mu
	k2 = k2j*Pk/N2
	dS2dt = -B2*S2 - k2*S2 + d*R2
	dE2dt = B2*S2 - c2*E2 + k2*S2
	dI2dt = c2*E2 - a2*I2 - mu2*I2
	dR2dt = a2*I2 - d*R2
	dM2dt = mu2*I2
    
    
	B3j = sum(Cij[2,:]*Ij)
	k3j = sum(Cij[2,:]*Ej)
    
	B3 = (B3j*Pb/N3)
	c3 = c
	a3 = (1-0.002)*a
	mu3 = 0.002*mu
	k3 = k3j*Pk/N3
	dS3dt = -B3*S3 - k3*S3 + d*R3
	dE3dt = B3*S3 - c3*E3 + k3*S3
	dI3dt = c3*E3 - a3*I3 - mu3*I3
	dR3dt = a3*I3 - d*R3
	dM3dt = mu3*I3
	
	B4j = sum(Cij[3,:]*Ij)
	k4j = sum(Cij[3,:]*Ej)
    
	B4 = (B4j*Pb/N4)
	c4 = c
	a4 = (1-0.002)*a
	mu4 = 0.002*mu
	k4 = k4j*Pk/N4 
	dS4dt = -B4*S4 - k4*S4 + d*R4
	dE4dt = B4*S4 - c4*E4 + k4*S4
	dI4dt = c4*E4 - a4*I4 - mu4*I4
	dR4dt = a4*I4 - d*R4
	dM4dt = mu4*I4
    
    
	B5j = sum(Cij[4,:]*Ij)
	k5j = sum(Cij[4,:]*Ej)
    
	B5 = (B5j*Pb/N5)
	c5 = c
	a5 = (1-0.004)*a
	mu5 = 0.004*mu
	k5 = k5j*Pk/N5 
	dS5dt = -B5*S5 - k5*S5 + d*R5
	dE5dt = B5*S5 - c5*E5 + k5*S5
	dI5dt = c5*E5 - a5*I5 - mu5*I5
	dR5dt = a5*I5 - d*R5
	dM5dt = mu5*I5
    
    
	B6j = sum(Cij[5,:]*Ij)
	k6j = sum(Cij[5,:]*Ej)
    
	B6 = (B6j*Pb/N6)
	c6 = c
	a6 = (1-0.013)*a
	mu6 = 0.013*mu
	k6 = k6j*Pk/N6 
	dS6dt = -B6*S6 - k6*S6 + d*R6
	dE6dt = B6*S6 - c6*E6 + k6*S6
	dI6dt = c6*E6 - a6*I6 - mu6*I6
	dR6dt = a6*I6 - d*R6
	dM6dt = mu6*I6
    
    
	B7j = sum(Cij[6,:]*Ij)
	k7j = sum(Cij[6,:]*Ej)
    
	B7 = (B7j*Pb/N7)
	c7 = c
	a7 = (1-0.036)*a
	mu7 = 0.036*mu
	k7 = k7j*Pk/N7 
	dS7dt = -B7*S7 - k7*S7 + d*R7
	dE7dt = B7*S7 - c7*E7 + k7*S7
	dI7dt = c7*E7 - a7*I7 - mu7*I7
	dR7dt = a7*I7 - d*R7
	dM7dt = mu7*I7
    
    
	B8j = sum(Cij[7,:]*Ij)
	k8j = sum(Cij[7,:]*Ej)
    
	B8 = (B8j*Pb/N8)
	c8 = c
	a8 = (1-0.114)*a
	mu8 = 0.114*mu
	k8 = k8j*Pk/N8 
	dS8dt = -B8*S8 - k8*S8 + d*R8
	dE8dt = B8*S8 - c8*E8 + k8*S8
	dI8dt = c8*E8 - a8*I8 - mu8*I8
	dR8dt = a8*I8 - d*R8
	dM8dt = mu8*I8
	return [dS1dt, dE1dt, dI1dt, dR1dt, dM1dt,
		dS2dt, dE2dt, dI2dt, dR2dt, dM2dt,
		dS3dt, dE3dt, dI3dt, dR3dt, dM3dt,
		dS4dt, dE4dt, dI4dt, dR4dt, dM4dt,
		dS5dt, dE5dt, dI5dt, dR5dt, dM5dt,
		dS6dt, dE6dt, dI6dt, dR6dt, dM6dt,
		dS7dt, dE7dt, dI7dt, dR7dt, dM7dt,
		dS8dt, dE8dt, dI8dt, dR8dt, dM8dt]
N = 23.6e6
N1 = 0.137*N
N2 = 0.146*N
N3 = 0.160*N
N4 = 0.162*N
N5 = 0.139*N
N6 = 0.115*N
N7 = 0.080*N
N8 = 0.061*N
I10 = 0
I20 = 0
I30 = 0
I40 = 1
I50 = 0
I60 = 0
I70 = 2
I80 = 1


x0 = [N1,0,I10,0,0,
      N2,0,I20,0,0,
      N3,0,I30,0,0,
      N4,0,I40,0,0,
      N5,0,I50,0,0,
      N6,0,I60,0,0,
      N7,0,I70,0,0,
      N8,0,I80,0,0]
t = np.linspace(1, 730, 1000)
x = odeint(Corona6, x0, t)

S1 = x[:,0]
E1 = x[:,1]
I1 = x[:,2]
R1 = x[:,3]
M1 = x[:,4]
CT1 = M1 + R1 + I1
S2 = x[:,5]
E2 = x[:,6]
I2 = x[:,7]
R2 = x[:,8]
M2 = x[:,9]
CT2 = M2 + R2 + I2
S3 = x[:,10]
E3 = x[:,11]
I3 = x[:,12]
R3 = x[:,13]
M3 = x[:,14]
CT3 = M3 + R3 + I3
S4 = x[:,15]
E4 = x[:,16]
I4 = x[:,17]
R4 = x[:,18]
M4 = x[:,19]
CT4 = M4 + R4 + I4
S5 = x[:,20]
E5 = x[:,21]
I5 = x[:,22]
R5 = x[:,23]
M5 = x[:,24]
CT5 = M5 + R5 + I5
S6 = x[:,25]
E6 = x[:,26]
I6 = x[:,27]
R6 = x[:,28]
M6 = x[:,29]
CT6 = M6 + R6 + I6
S7 = x[:,30]
E7 = x[:,31]
I7 = x[:,32]
R7 = x[:,33]
M7 = x[:,34]
CT7 = M7 + R7 + I7
S8 = x[:,35]
E8 = x[:,36]
I8 = x[:,37]
R8 = x[:,38]
M8 = x[:,39]
CT8 = M8 + R8 + I8

I = I1 + I2 + I3 + I4 + I5 + I6 + I7 + I8
M = M1 + M2 + M3 + M4 + M5 + M6 + M7 + M8
CT = CT1 + CT2 + CT3 + CT4 + CT5 + CT6 + CT7 + CT8
	
	
	
############################



graph1 = go.Scatter(
	x=t,
	y=I,
	name = "Infectados"
)

graph2 = go.Scatter(
	x=t,
	y=M,
	name = "Mortos"
)

graph3 = go.Scatter(
	x=t,
	y=0.05*CT,
	name = "Casos graves cumulativos"
)



dat = [graph1,graph2,graph3]

beer_fig = go.Figure(data=dat)

beer_fig.update_layout(
    title="Modelo SEIRDS com divisao de idades",
    xaxis_title="Tempo (dias)",
    yaxis_title="Numero de casos",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


##############TestZone###############

#####################################


########### Set up the layout
app.layout = html.Div(style ={'backgroundColor': colors['background']}, children=[
    html.H1(
	    children = myheading,
	    style={
		    'textAlign': 'center',
		    'color': colors['text']
	    }
		 
    ),
    html.Div(children=' Uma ferramenta interativa para o estudo da pandemia', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
	
    html.Div(
        children=html.Img(
            src="https://raw.githubusercontent.com/YokoSenju/flying-dog-beers/master/image.png",
            style={
                'maxWidth': '100%',
                'maxHeight': '100%',
                'marginLeft': 'auto',
                'marginRight': 'auto'
            }
        ),
        style={
            'width': 100,
            'height': 50,
            'border': 'thin grey solid'
        }
    ),	
    dcc.Graph(
        id='flyingdog',
        figure={'data': [
                {'x': t, 'y': I, 'name': 'Infectados'},
		{'x': t, 'y': 0.05*CT, 'name': 'Numero cumulativo de casos criticos'},
		{'x': t, 'y': M, 'name': 'Mortos'}
            ],
	       'layout': {
			'plot_bgcolor': colors['background'],
                	'paper_bgcolor': colors['background'],
                	'font': {
                    		'color': colors['text']
			}
	       }
	}         
	     
    ),
    html.A('Github', href=githublink),
    html.Br(),
    html.A('Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
