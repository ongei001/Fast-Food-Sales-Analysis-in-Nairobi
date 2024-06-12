import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv(r'C:\Users\carso\Downloads\fast_food_sales_nairobi.csv', parse_dates=['Date'])

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Fast Food Sales Analysis in Nairobi", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(id='line-plot', style={'height': '300px'}),
        dcc.Graph(id='bar-plot', style={'height': '300px'}),
        dcc.Graph(id='pie-chart', style={'height': '300px'}),
        dcc.Graph(id='heatmap', style={'height': '300px'}),
        dcc.Graph(id='box-plot', style={'height': '300px'}),
        dcc.Graph(id='restaurant-bar-plot', style={'height': '300px'}),
        dcc.Graph(id='scatter-plot', style={'height': '300px'})
    ], style={'columnCount': 2, 'width': '100%', 'display': 'inline-block'})
])

# Define callback functions

# Line Plot: Sales Trend Over Time
@app.callback(
    Output('line-plot', 'figure'),
    [Input('line-plot', 'id')]
)
def update_line_plot(_):
    fig = px.line(df, x='Date', y='Sales', title='Sales Trend Over Time')
    return fig

# Bar Plot: Total Sales by Product
@app.callback(
    Output('bar-plot', 'figure'),
    [Input('bar-plot', 'id')]
)
def update_bar_plot(_):
    product_sales = df.groupby('Product')['Sales'].sum().reset_index()
    fig = px.bar(product_sales, x='Product', y='Sales', title='Total Sales by Product')
    return fig

# Pie Chart: Sales Distribution by Category
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('pie-chart', 'id')]
)
def update_pie_chart(_):
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    fig = px.pie(category_sales, values='Sales', names='Category', title='Sales Distribution by Category')
    return fig

# Heatmap: Correlation between Variables
@app.callback(
    Output('heatmap', 'figure'),
    [Input('heatmap', 'id')]
)
def update_heatmap(_):
    corr_matrix = df.corr()
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='Viridis'))
    fig.update_layout(title='Correlation Heatmap')
    return fig

# Box Plot: Sales Distribution Across Regions
@app.callback(
    Output('box-plot', 'figure'),
    [Input('box-plot', 'id')]
)
def update_box_plot(_):
    fig = px.box(df, x='Region', y='Sales', title='Sales Distribution Across Regions')
    return fig

# Bar Plot: Total Sales by Restaurant
@app.callback(
    Output('restaurant-bar-plot', 'figure'),
    [Input('restaurant-bar-plot', 'id')]
)
def update_restaurant_bar_plot(_):
    restaurant_sales = df.groupby('Restaurant')['Sales'].sum().reset_index()
    fig = px.bar(restaurant_sales, x='Restaurant', y='Sales', title='Total Sales by Restaurant')
    return fig

# Scatter Plot: Quantity Sold by Region and Product
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-plot', 'id')]
)
def update_scatter_plot(_):
    # Change 'Region' to numerical value for scatter plot
    df['Region'] = df['Region'].astype('category').cat.codes
    fig = px.scatter(df, x='Region', y='Quantity', color='Product', title='Quantity Sold by Region and Product')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
