from urllib import request
from bs4 import BeautifulSoup

def GetKernel():
    chk_kernel_mainline = []
    chk_kernel_stable = []
    chk_kernel_longterm = []
    page = request.urlopen(f'https://www.kernel.org/')
    soup_releases_table = BeautifulSoup(page, features="html.parser")
    releases_table = soup_releases_table.findAll('table', attrs={'id' : 'releases'})
    soup_table_rows = BeautifulSoup(str(releases_table[0]), features="html.parser")
    table_rows = soup_table_rows.findAll('tr', attrs={'align' : 'left'})
    for row in table_rows:
        soup_row = BeautifulSoup(str(row), features="html.parser")
        row_entries = soup_row.findAll('td')
        if row_entries[0].text == "mainline:":
            chk_kernel_mainline.append(row_entries[1].text)
        if row_entries[0].text == "stable:":
            chk_kernel_stable.append(row_entries[1].text)
        if row_entries[0].text == "longterm:":
            chk_kernel_longterm.append(row_entries[1].text)

    return (chk_kernel_mainline, chk_kernel_stable, chk_kernel_longterm)
