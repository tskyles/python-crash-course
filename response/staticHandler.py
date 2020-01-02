import os
from response.requestHandler import RequestHandler

class StaticHandler(RequestHandler):
  def __init__(self):
    self.filetypes = {
      ".js" : "text/javascript",
      ".css" : "text/css",
      ".jpg" : "image/jpeg",
      ".png" : "image/png",
      "notfound" : "text/plain"
    }
  
  def find(self, file_path):
    split_path = os.path.splitext(file_path)
    extention = split_path[1]

    try:
      if extention in (".jpg", ".jpeg", ."png"):
        self.contents = open("public{}".format(file_path), 'rb')
      else:
        self.contents = open("public{}".format(file_path), 'r')

      self.setContentType(extention)
      self.setStatus(200)
      return True
    except:
      self.setContentType('notfound')
      self.setStatus(404)
      return False

  def setContentType(self, ext):
    self.contentType = self.filetypes[ext]