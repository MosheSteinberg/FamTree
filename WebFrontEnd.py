# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 13:57:11 2020

@author: MS13
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import familytreemaker as ftm
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
		'background': '#111111',
		'text': '#7FDBFF',
		'lightGreen': '#90ee90'}

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(children='Family Tree Builder', style={'textAlign': 'center', 'color': colors['lightGreen']}),

    html.Div(children='''
        Use this application to input your relatives and receive a family tree.
    ''',
	style={'textAlign': 'center', 'color':colors['lightGreen']}),

	html.Div(style={'textAlign':'center', 'backgroundColor':'#ffffff'},children=[
			dcc.Input(id='Ancestor', type='text', value='GGCharlie'),
			html.Button(id='ShowTree', n_clicks=0,children='Show tree'),
			html.Div(id='family-tree')])
])

@app.callback(Output('family-tree', 'children'),
			[Input('ShowTree', 'n_clicks')],
			[State('Ancestor', 'value')])
def update_output(n_clicks, Ancestor):
	
	return Ancestor + "\'s tree"

if __name__ == '__main__':
    app.run_server(debug=True)