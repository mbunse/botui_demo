#!/bin/bash

set -Eeuo pipefail

function print_help {
    echo "Available options:"
    echo " start  - Start Rasa Core server"
    echo " help   - Print this help"
    echo " run    - Run an arbitrary command inside the container"
}

case ${1} in
    start)
        exec rasa run actions -p 5055 &
        exec python -m rasa run -m models_de/model.tar.gz --port $PORT --cors "*" --credentials credentials.yml --endpoints endpoints.yml
        ;;
    run)
        exec "${@:2}"
        ;;
    *)
        print_help
        ;;
esac