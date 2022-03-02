#!/bin/bash

set -Eeuo pipefail

function print_help {
    echo "Available options:"
    echo " start  - Start Rasa action server"
    echo " help   - Print this help"
    echo " run    - Run an arbitrary command inside the container"
}

case ${1} in
    start)
        exec rasa run actions -p 5055 &
        ;;
    run)
        exec "${@:2}"
        ;;
    *)
        print_help
        ;;
esac