import os
import sys

def change_base_dir():
    this_path = os.path.split(__file__)[0]
    if this_path not in sys.path:
        sys.path.insert(0,this_path)
    os.chdir(this_path)
    this_path = os.path.split(this_path)[0]
    if this_path not in sys.path:
        sys.path.insert(0,this_path)

change_base_dir()

import p17data.Config
import p17data.Scraping
import p23control.Scraping
import tools.p23control.Database

soughts = p23control.Scraping.scrap('master')
version = p17data.Scraping.versions[p17data.Config.version]
selectQuery1 = version['master']['selectQuery1']
insertQuery1 = version['master']['insertQuery1']
insertQuery2 = version['master']['insertQuery2']
for sought in soughts:
    print(sought)
    if sought['author'][:3] == 'by ':
        sought['author'] = sought['author'][3:]
    tools.p23control.Database.execute(insertQuery1,[sought['author']])
    author_id = tools.p23control.Database.query(selectQuery1,[sought['author']])[0][0]
    print(author_id)
    tools.p23control.Database.execute(insertQuery2,(sought['url'],author_id))
    tools.p23control.Database.execute('commit',[])

