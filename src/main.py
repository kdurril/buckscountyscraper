import daily
import parse
import db

#create a list of urls for records, 100 record at a time 
url = daily.bucks(inspect_id=928801)
#make request to bucks county site
#store to file if to_file is True
records = []
for record in url:
    records.append(daily.get_txt(**record, to_file=False))
#parse the html
prsd = [parse.web_gather(inspection) for inspection in records]
#send to db
db.json2db(input_data=prsd, database='db', user='user', password=None)

#records = daily.get_txt(**next(record), to_file=False)


