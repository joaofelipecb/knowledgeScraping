versions = {}
versions['0.0.0.1.1'] = {}
versions['0.0.0.1.1']['master'] = {}
versions['0.0.0.1.1']['master']['url'] = 'https://www.alphasights.com/news/alphasights-blog?locale=en'
versions['0.0.0.1.1']['master']['begin'] = '''<div class=\'container search_results\'>
<div>'''
versions['0.0.0.1.1']['master']['end'] = '''</div>
</div>

'''
versions['0.0.0.1.1']['master']['separator'] = '''</div>
<div class=\'col-sm-6 col-md-4 col-xs-12\'>'''
versions['0.0.0.1.1']['master']['seeks'] = {}
versions['0.0.0.1.1']['master']['seeks']['url'] = {
    'begin':'<a href="',
    'end':'">'
    }
versions['0.0.0.1.1']['master']['seeks']['author'] = {
    'begin':'''</li>
<li>
by
''',
    'end':'''
</li>'''
    }

versions['0.0.0.1.1']['master']['selectQuery1'] = 'select person_id from people where person_name = %s'
versions['0.0.0.1.1']['master']['insertQuery1'] = 'insert into people(person_name) values(%s) on conflict do nothing'
versions['0.0.0.1.1']['master']['insertQuery2'] = 'insert into articles(article_url,person_id,article_scraped) values(%s,%s,FALSE)'

versions['0.0.0.1.1']['detail'] = {}
versions['0.0.0.1.1']['detail']['url'] = 'https://www.alphasights.com'
versions['0.0.0.1.1']['detail']['begin'] = '''<li>TAGS:</li>'''
versions['0.0.0.1.1']['detail']['end'] = '''</ul>'''
versions['0.0.0.1.1']['detail']['separator'] = '''</li>
<li class='blog-tag'>'''
versions['0.0.0.1.1']['detail']['seeks'] = {}
versions['0.0.0.1.1']['detail']['seeks']['tag'] = {
    'begin':'">',
    'end':'</a>'
    }

versions['0.0.0.1.1']['detail']['selectQuery1'] = 'select article_id, article_url, person_id from articles where article_scraped = false order by article_id'
versions['0.0.0.1.1']['detail']['insertQuery1'] = 'insert into tags(tag_name) values(%s) on conflict do nothing'
versions['0.0.0.1.1']['detail']['selectQuery2'] = 'select tag_id from tags where tag_name = %s'
versions['0.0.0.1.1']['detail']['insertQuery2'] = 'insert into tags_x_people(tag_id,person_id) values(%s,%s) on conflict do nothing'
versions['0.0.0.1.1']['detail']['updateQuery1'] = 'update articles set article_scraped = true where article_id = %s'
