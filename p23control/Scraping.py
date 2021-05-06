import p17data.Config
import p17data.Scraping

def scrap(profile,url):
    import p24command.Scraping
    escope = {}
    p24command.Scraping.scrap_init(escope,profile,url)
    for escope['i'] in range(0,len(escope['parts'])):
        scrap_seek(escope)
    return escope['soughts']

def scrap_seek(escope):
    import p24command.Scraping
    p24command.Scraping.scrap_seek_init(escope)
    version = p17data.Scraping.versions[p17data.Config.version]
    for escope['seek'] in escope['seeks']:
        p24command.Scraping.scrap_seek_each(escope)
    p24command.Scraping.scrap_seek_finish(escope)

