import sqlite3
import pandas as pd
import weasyprint
from weasyprint import CSS

def cleanup_weekly(query, con, channel_id, client):
    df = pd.read_sql_query(query, con)
    to_html_pretty(df, filename='./reports/weekly_out.html', title='Cleanups')
    weasyprint.HTML('./reports/weekly_out.html').write_pdf('./reports/weekly_cleanups.pdf')
    client.files_upload(channels=channel_id, inital_comment="Gabba Gool", file='./reports/weekly_cleanups.pdf')

def takedown_weekly(query, con, channel_id, client):
    df = pd.read_sql_query(query, con)
    to_html_pretty(df, filename='./reports/weekly_takedown_out.html', title='Takedowns')
    weasyprint.HTML('./reports/weekly_takedown_out.html').write_pdf(target='./reports/weekly_takedowns.pdf')
    client.files_upload(channels=channel_id, inital_comment="Gabba Gool", file='./reports/weekly_takedowns.pdf')

def takedowns_display(query, con, user_id, client):
    df = pd.read_sql_query(query, con)
    to_html_pretty(df, filename='./reports/takedowns_display_out.html', title='Takedowns Database')
    weasyprint.HTML('./reports/takedowns_display_out.html').write_pdf('./reports/takedowns_display_out.pdf', stylesheets=[CSS(string=PAGE_SIZE)])
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/takedowns_display_out.pdf')

def cleanups_display(query, con, user_id, client):
    df = pd.read_sql_query(query, con)
    to_html_pretty(df, filename='./reports/cleanups_display_out.html', title='Cleanups Database')
    weasyprint.HTML('./reports/cleanups_display_out.html').write_pdf('./reports/cleanups_display_out.pdf', stylesheets=[CSS(string=PAGE_SIZE)])
    client.files_upload(channels=user_id, inital_comment="Gabba Gool", file='./reports/cleanups_display_out.pdf')

def to_html_pretty(df, filename, title=''):
    ht = ''
    if title != '':
        ht += '<h2> %s </h2>\n' % title
    ht += df.to_html(classes='wide', escape=False)

    with open(filename, 'w') as f:
         f.write(HTML_TEMPLATE1 + ht + HTML_TEMPLATE2)

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
PAGE_SIZE = '''
@page { size: A1; margin: 1cm }
'''