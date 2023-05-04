web: gunicorn --preload -b 127.0.0.1:5000 --chdir /app/client __init__:app
api: gunicorn --preload -b 127.0.0.1:5001 --chdir /app/server __init__:app