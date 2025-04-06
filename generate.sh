docker run --rm -it --user $(id -u):$(id -g) -v ${PWD}:/app/output mcr.microsoft.com/openapi/kiota generate --language go -n github.com/cedana/cedana-go-sdk -d /app/openapi.json
