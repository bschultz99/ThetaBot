# pylint: disable=line-too-long
"""PDF Exporter"""
import pandas as pd
import pdfkit

options = {
    'page-size': 'A1',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}




def cleanup_weekly(query, con, channel_id, client):
    """Generates Weekly Cleanups PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/weekly_out.html', title='Cleanups')
    pdfkit.from_file('./reports/weekly_out.html','./reports/weekly_cleanups.pdf', options=options)
    client.files_upload(channels=channel_id, inital_comment="Gabba Gool", file='./reports/weekly_cleanups.pdf')

def takedown_weekly(query, con, channel_id, client):
    """Generates Weekly Takedown PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/weekly_takedown_out.html', title='Takedowns')
    pdfkit.from_file('./reports/weekly_takedown_out.html','./reports/weekly_takedowns.pdf', options=options)
    client.files_upload(channels=channel_id, inital_comment="Gabba Gool", file='./reports/weekly_takedowns.pdf')

def takedowns_display(query, con, user_id, client):
    """Generates Takedown Database PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/takedowns_display_out.html', title='Takedowns Database')
    pdfkit.from_file('./reports/takedowns_display_out.html','./reports/takedowns_display_out.pdf', options=options)
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/takedowns_display_out.pdf')

def cleanups_display(query, con, user_id, client):
    """Generates Cleanups Database PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/cleanups_display_out.html', title='Cleanups Database')
    pdfkit.from_file('./reports/cleanups_display_out.html','./reports/cleanups_display_out.pdf', options=options)
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/cleanups_display_out.pdf')

def fines_display(query, con, user_id, client):
    """Generates Fines Database PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/fines_display_out.html', title='Fines Database')
    pdfkit.from_file('./reports/fines_display_out.html','./reports/fines_display_out.pdf', options=options)
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/fines_display_out.pdf')

def reconcilliations_display(query, con, user_id, client):
    """Generates Reconcilliations Database PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/reconcilliations_display_out.html', title='Reconcilliations Database')
    pdfkit.from_file('./reports/reconcilliations_display_out.html','./reports/reconcilliations_display_out.pdf', options=options)
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/reconcilliations_display_out.pdf')

def naughtylist_display(query, con, user_id, client):
    """Generates Naughty List Database PDF"""
    data_frame = pd.read_sql_query(query, con)
    to_html_pretty(data_frame, filename='./reports/naughty_display_out.html', title='Naughty Database')
    pdfkit.from_file('./reports/naughty_display_out.html','./reports/naughty_display_out.pdf', options=options)
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/naughty_display_out.pdf')


def to_html_pretty(data_frame, filename, title=''):
    "Generates Pretty HTMl which is used to convert to PDF"
    html_frame = ''
    if title != '':
        html_frame += f'<h2> {title} </h2>\n'
    html_frame += data_frame.to_html(classes='wide', escape=False)

    with open(filename, 'w', encoding="utf-8") as file:
        file.write(HTML_TEMPLATE1 + html_frame + HTML_TEMPLATE2)

HTML_TEMPLATE1 = '''
<html>
<head>
<style>
  h2 {
    text-align: center;
    font-family: Helvetica, Arial, sans-serif;
  }
  table { 
    margin-left: auto;
    margin-right: auto;
  }
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  tr:nth-child(even) {
    background-color: #d1caca93;
  }
  th, td {
    padding: 5px;
    text-align: center;
    font-family: Helvetica, Arial, sans-serif;
    font-size: 90%;
  }
  table tbody tr:hover {
    background-color: #dddddd;
  }
  .wide {
    width: 90%; 
  }
</style>
</head>
<body>
'''

HTML_TEMPLATE2 = '''
</body>
</html>
'''