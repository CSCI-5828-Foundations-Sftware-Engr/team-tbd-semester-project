web: gunicorn --preload -b 0.0.0.0:5000 --chdir /app/client __init__:app
api: gunicorn --preload -b 0.0.0.0:5001 --chdir /app/server __init__:app