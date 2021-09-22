import pandas as pd 
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


app = dash.Dash(__name__)

# Dataframe of the books created using pandas
books = pd.read_csv("./dataset/books_dash/bestsellers with categories.csv")
print(books.head())
# print(books["Genre"].value_counts())
genre_df = books["Genre"].value_counts().rename_axis("Types").reset_index(name="counts")
fig = px.bar(genre_df, x="Types", y="counts", barmode="group")

scatter_chart = px.scatter(books, x='User Rating', y="Price", color="Genre")

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
box_plot = px.box(books, x="Price", y="Reviews",color="Genre")

author_book_df = books["Author"].value_counts()[:15].rename_axis("Author_Name").reset_index(name="Book_Count")
bar_author_book_plot = px.bar(author_book_df, x="Author_Name", y="Book_Count",text="Book_Count",barmode="group")

author_vs_his_reviews = books.loc[books["Author"]=="Jeff Kinney"]
author_bar_chart = px.bar(author_vs_his_reviews, x="Name", y="Reviews",text="Reviews")

app.layout = html.Div(children=[
    html.H1(children="Analysis of Amazon Books selling dataset"),
    html.Div(children=[html.H2(children="Value counts of Genre")]),
    dcc.Graph(
        id='bar_graph',
        figure=fig
    ),
    html.Div(
        children=[
            html.H2(children="Comparison between price and reviews")
            ]
    ),
    dcc.Graph(
         id="Scatter_graph",
        figure=scatter_chart
    ),
    html.Div(children=[
        html.H2(children="Comparison between Reviews and Price")
        ]),
    dcc.Graph(
        id="box_plot",
        figure=box_plot
    ),
    html.Div(children=[
        html.H2(children="Author vs Book count")
        ]),
    dcc.Graph(
        id="bar_author_book",
        figure=bar_author_book_plot
    ),
    html.Div(children=[
        html.H2(children="Author Jeff Kinney vs Reviews")
        ]),
    dcc.Graph(
        id="author_vs_his_books",
        figure=author_bar_chart
    )
    
])


if __name__ == '__main__':
    app.run_server(debug=True)