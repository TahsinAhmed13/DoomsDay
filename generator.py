#!/usr/bin/python3

import cgi
import cgitb

import dates

cgitb.enable()
print('content-type: text/html\n')

def get_calendar_template(path: str) -> str: 
    try: 
        f = open(path, 'r')
        html = f.read()
        f.close()
        return html
    except: 
        return '<html><body>could not read template</body></html>'

def make_calendar(date: dates.GregorianDate) -> str: 
    template = get_calendar_template('./calendar.html')
    template = template.replace('<!--header-->', date.get_header())

    code = date.get_weekday_code() 
    numbers = [['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','',''],['','','','','','','']]
    week = 0
    weekday = (code - date.day + 1) % 7 

    for i in range(1, date.get_max_days() + 1):
        numbers[week%5][weekday%7] = i
        week += (weekday + 1) // 7
        weekday = (weekday + 1) % 7

    for i in numbers: 
        for j in i:
            template = template.replace('<!--num-->', str(j), 1)

    code = (code - date.day + 1) % 7 + (date.day - 1)
    template = template.replace('/*week*/', str(19 + 14 * (code // 7 % 5)))
    template = template.replace('/*day*/', str(10 + 11.25 * (code % 7)))

    return template

def main(): 
    form = cgi.FieldStorage()
    try:
        month = int(form.getvalue('month'))
        day = int(form.getvalue('day'))
        year = int(form.getvalue('year'))
        date = dates.GregorianDate(month, day, year)
        if date.validate(): 
            print(make_calendar(date))
        else: 
            print(get_calendar_template('./invalid.html'))
    except: 
        print(get_calendar_template('./invalid.html'))

main()
