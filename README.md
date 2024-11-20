🎲 Sistema Gacha en Python
Un sistema gacha escalable implementado en Python, que utiliza una base de datos para almacenar personajes y probabilidades, con lógica dinámica de ajustes en las tiradas. Este proyecto está diseñado para ser extensible y fácil de mantener.

🚀 Características
Tiradas garantizadas:
Un personaje de 3 estrellas asegurado cada 10 tiradas.
Un personaje de 4 estrellas asegurado cada 25 tiradas.
Un personaje de 5 estrellas asegurado cada 40 tiradas.
Ajuste dinámico de probabilidades:
La probabilidad de obtener un personaje de 5 estrellas aumenta progresivamente a medida que te acercas a la tirada 50.
Base de datos integrada:
Personajes y probabilidades se almacenan en una base de datos SQLite (puede cambiarse a PostgreSQL, MySQL, etc.).
Estructura modular:
Organización clara del código para facilitar la ampliación y el mantenimiento.
📂 Estructura del Proyecto
bash
Copiar código
gacha_project/
├── main.py             # Archivo principal para ejecutar el sistema gacha
├── requirements.txt    # Lista de dependencias del proyecto
├── config.py           # Configuración global (URL de la base de datos)
├── models/             # Modelos de la base de datos
│   ├── __init__.py
│   └── personaje.py
├── controllers/        # Lógica del sistema gacha
│   ├── __init__.py
│   └── sistema_gacha.py
├── database/           # Gestión de la base de datos
│   ├── __init__.py
│   └── db.py
└── scripts/            # Scripts de utilidad
    ├── __init__.py
    └── agregar_personajes.py
🛠️ Instalación
Clona el repositorio:

bash
Copiar código
git clone https://github.com/tu-usuario/sistema-gacha.git
cd sistema-gacha
Crea un entorno virtual e instala las dependencias:

bash
Copiar código
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
Inicializa la base de datos y agrega personajes iniciales:

bash
Copiar código
python scripts/agregar_personajes.py
Ejecuta el sistema gacha:

bash
Copiar código
python main.py
⚙️ Configuración
El archivo config.py contiene la configuración del proyecto. Puedes cambiar la URL de la base de datos según tus necesidades.

Ejemplo de configuración:

python
Copiar código
DATABASE_URL = "sqlite:///gacha.db"  # Cambia a PostgreSQL, MySQL, etc., si es necesario.
🧪 Ejemplo de Uso
Ejecuta main.py para simular 50 tiradas del sistema gacha:

bash
Copiar código
python main.py
Ejemplo de salida:

less
Copiar código
Tirada 1: ¡Has obtenido a Héroe 1 (1★)!
Tirada 2: ¡Has obtenido a Héroe 3 (3★)!
Tirada 10: ¡Has obtenido a Héroe 3 (3★)! (Garantizado)
Tirada 25: ¡Has obtenido a Héroe 4 (4★)! (Garantizado)
Tirada 40: ¡Has obtenido a Héroe 5 (5★)! (Garantizado)
...
🛡️ Contribuciones
¡Las contribuciones son bienvenidas! Si deseas colaborar, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu funcionalidad o corrección (git checkout -b mi-nueva-funcionalidad).
Haz un commit de tus cambios (git commit -m 'Añadida nueva funcionalidad').
Sube tus cambios a tu fork (git push origin mi-nueva-funcionalidad).
Abre un Pull Request.
📜 Licencia
Este proyecto está bajo la licencia MIT.

🌟 Próximos Pasos
Implementar un sistema de eventos con personajes exclusivos.
Agregar más estadísticas y atributos a los personajes.
Integrar una interfaz gráfica o API para gestionar el sistema.
¡Listo! Puedes personalizar este archivo según tus necesidades. 😊