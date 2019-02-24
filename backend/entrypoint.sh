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
        exec python -m rasa_core_sdk.endpoint -p 5055 --actions actions &
        exec python -m rasa_core.run -d model/dialogue -u model/nlu --port $PORT --cors "*" --credentials credentials.yml  --endpoints endpoints.yml
        ;;
    run)
        exec "${@:2}"
        ;;
    *)
        print_help
        ;;
esac