rm -rf models/ v1/ v2/ api_client.go kiota-lock.json
docker run --rm -it --user $(id -u):$(id -g) -v "${PWD}":/app/output mcr.microsoft.com/openapi/kiota generate --language go -n github.com/cedana/cedana-go-sdk -d /app/output/openapi.json
