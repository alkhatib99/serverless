from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
      s=self.path
      url_components=parse.urlsplit(s)
      query_list=parse.parse_qsl(url_components.query)
      dic=dict(query_list)

      name=dict.get("name")

      age=dict.get("age")

      if name:
          msg=f'Aloha{name}'
      else:
          msg="Aloha stranger"

      msg+=f'Greetings from Python version {platform.python_version()}'  
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()
      self.wfile.write(msg.encode())
      