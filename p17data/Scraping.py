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
versions['0.0.0.1.1']['master']['insertQuery2'] = 'insert into articles(article_url,person_id) values(%s,%s)'
