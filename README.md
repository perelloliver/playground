## For development with auto-reload...

docker run -p 8000:8000 -v $(pwd):/app playground

## Otherwise..

docker build -t playground .

docker run -p 8000:8000 playground