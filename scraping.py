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

def master():
    import p17data.Config
    import p17data.Scraping
    import p23control.Scraping
    import tools.p23control.Database

    version = p17data.Scraping.versions[p17data.Config.version]
    url = version['master']['url']
    soughts = p23control.Scraping.scrap('master',url)
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

def detail():
    import p17data.Config
    import p17data.Scraping
    import p23control.Scraping
    import tools.p23control.Database

    version = p17data.Scraping.versions[p17data.Config.version]
    url = version['detail']['url']
    selectQuery1 = version['detail']['selectQuery1']
    selectQuery2 = version['detail']['selectQuery2']
    insertQuery1 = version['detail']['insertQuery1']
    insertQuery2 = version['detail']['insertQuery2']
    updateQuery1 = version['detail']['updateQuery1']
    articles = tools.p23control.Database.query(selectQuery1,[])
    for article in articles:
        print(article)
        soughts = p23control.Scraping.scrap('detail',url+article[1])
        print(soughts)
        for sought in soughts:
            print(sought)
            tools.p23control.Database.execute(insertQuery1,[sought['tag']])
            tag_id = tools.p23control.Database.query(selectQuery2,[sought['tag']])[0][0]
            print(tag_id)
            tools.p23control.Database.execute(insertQuery2,[tag_id,article[2]])
            tools.p23control.Database.execute(updateQuery1,[article[0]])
        tools.p23control.Database.execute('commit',[])

if sys.argv[1] == 'master':
    master()

if sys.argv[1] == 'detail':
    detail()
