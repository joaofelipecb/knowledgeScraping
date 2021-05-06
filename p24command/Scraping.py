import requests
import p17data.Config
import p17data.Scraping

def scrap_init(escope,profile,url):
    escope['profile'] = profile
    escope['url'] = url
    version = p17data.Scraping.versions[p17data.Config.version]
    escope['seeks'] = version[profile]['seeks']
    response = requests.get(url)
    text = response.text
    part = text.split(version[profile]['begin'])[1]
    part = part.split(version[profile]['end'])[0]
    escope['parts'] = part.split(version[profile]['separator'])
    escope['soughts'] = []

def scrap_seek_init(escope):
    escope['sought'] = {}

def scrap_seek_each(escope):
    part = escope['parts'][escope['i']]
    seek = escope['seeks'][escope['seek']]
    part = part.split(seek['begin'])[1]
    part = part.split(seek['end'])[0]
    escope['sought'][escope['seek']] = part

def scrap_seek_finish(escope):
    escope['soughts'].append(escope['sought'])

