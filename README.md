Para usar este programa se requiere:
pip 24.2
pymong 4.10.1
python 3.12.8

Para hacerlo de forma mas sencilla se requiere instalar miniconda "ultima version"
Luego de haber instalado abrir shell de anaconda y colocar los siguientes comandos:

# Crear el entorno con Python 3.12
conda create --name Fase_tres python=3.12

# Activar el entorno
conda activate Fase_tres

# Instalar pymongo para la conexión a MongoDB
conda install pymongo

# Tambien se puede usar pip  para instalr pymongo
pip install pymongo

# Verificar la instalación
python --version
pip list
conda list


Luego de haber creado el entorno virtual tenemos que descargar el respositoro del programa en GitHub y configurarlo
con el interprete de miniconda o conda llamado "Fase_3" para aplicar las dependencias o librerias  necesarias para este programa.

Links para desarrollar estos pasos:
  https://docs.anaconda.com/miniconda/
  https://www.youtube.com/watch?v=aE7qxfgubS8
  https://www.youtube.com/watch?v=roTSOa4s5gA

# Hacer restauracion de ProtoDEVDB.zip en MongoDB
Descargar el archivo comprmido ProtoDEVDB.zip para poder crear la base de datos e interactuar con ella.
ProtoDEVDB.zip Es un backup de la base de datos ProtoDEVDB.

NOTA!  
Este programa puede usarse en cualquier ide que se pueda aplicar los interpretes de entornos virtuales conda o que acepte varios interpretes como:
  Pycharm
  Visual Studio Code
