import facebook

mytoken = 'EAACEdEose0cBACNDhlmtoD8cY1nDuZBPIClQKs9yPcD1HBc0QUXv2EsufWKkvkOzS9byd5cDiugh3OVZA7QzCrZBpPhrDuuMoSyA84DeAESKY6XowqrLhohgVn1CLnF8i5FQwHadrqZAalNpZBIY3CnpiKKwJsQi8ZAIuazp088jD9PmKkRrUtYO1DNtZBA9tymgk38I9v8S8Eg34LcIDpy'

graph = facebook.GraphAPI(access_token=mytoken)

profile = graph.get_object(id='100000173490566')

posts = graph.get_connections(id='100000173490566',connection_name='posts')
print (profile['name'])
print (posts['data'])
'''
for posts in posts['data']:
    try:
        graph.put_object(posts['id'],'like')
        print('Like ' + posts['message'])
    except:
        continue
        '''