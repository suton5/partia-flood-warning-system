import plotly.plotly as py
import plotly.tools as tls
tls.set_credentials_file(username='suton5', api_key='zBB1uvWgEDy9tGpOIUyy')
import pandas as pd

df = pd.read_csv('/Users/Sujay/partia-flood-warning-sytem/station_coord.csv')
df.head()

df['text'] = df['Station'] + ', ' + df['Town'] + ', ' + df['River'].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]


data = [ dict(
        type = 'scattergeo',
        locationmode = 'Country Names',
        lon = df['Long'],
        lat = df['Lat'],
        text = df['text'],
        mode = 'markers',
        marker = dict( 
            size = 8, 
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = df['High Level'].min(),
            color = df['High Level'],
            cmax = df['High Level'].max(),
            colorbar=dict(
                title="Peak water levels Feb 2017"
            )
        ))]

layout = dict(
        title = 'River monitoring stations in 2017<br>(Hover for station name, town and river)',
        colorbar = False,   
        geo = dict(
            scope='europe',
            projection=dict( type='Natural Earth' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5        
        ),
    )

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='stations' )
