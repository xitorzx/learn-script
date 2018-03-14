import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAGucrWhOU9GiQB1YZBJTBHcyN8WuZApUWfXEHrpNJAcyjaP7BawJ1fZAVX7f8htbhy2be6w2umDTTR5TejPMjgOyBKedn7ZAHmqYptRTr1FEWGpgl69XfZBZBBsXZAgCTB0Nc1d35PvQU0ZBq0TD7UGRbIRUIRDq9VSgdqsuZCyvVrIFImRMy6ObWsrei7dk4ZB2YsjnkZA78wL')

attachment =  {
    'name':'Post Test',
    'caption': 'Check out this example',
    'description': 'This is a longer description of the attachment',
}

graph.put_wall_post(message='Hello! Graph Test',attachment=attachment)