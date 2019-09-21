#list with website names
url=['www.annauniv.edu', 'www.google.com','www.ndtv.com',
'www.website.org', 'www.bis.org.in', 'www.rbi.org.in']

#function to do sorting
def cus_sort(val):
    arr={'edu':1,'com':2,'org':3,'in':4}
    return arr.get(val.split('.')[-1])
    
#Customer Sort
url.sort(key=cus_sort)
print(url)
