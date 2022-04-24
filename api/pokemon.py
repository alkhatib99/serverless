from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        poke = self.path
        url_comp = parse.urlsplit(poke)
        query_string_list = parse.parse_qsl(url_comp.query)
        dic = dict(query_string_list)
        
        if 'poke' in dic:
            url = 'https://pokeapi.co/api/v2/pokemon/'
            r = requests.get(url + 'poke')
            data = r.json()
            pokemon = []
            
            for monster in data:
                select_stats = data['stats'][0]
                pokemon.append(select_stats)
            message = str(select_stats)
        else:
            message = "Enter pokemon name"
            
            
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        
        self.wfile.write(message.encode())
        return