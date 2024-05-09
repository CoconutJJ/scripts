#!/bin/bash

# Modify this to your path to binary executable
EXE_NAME="a.out"
EXEC_PATH=""

_load_payload() {
    tar -cjf - $1 | base64 | fold >>$0
}

_decompress_payload() {
    if [ -n "$EXEC_PATH" ]; then
        return
    fi

    PAYLOAD_LINE=$(grep -n "__PAYLOAD__" $0 | tail -n 1 | cut -d: -f1)
    BINARY_LINE=$(($PAYLOAD_LINE + 1))
    tail -n +${BINARY_LINE} $0 | base64 -d | tar -xjf - -C $1
    EXEC_PATH="$1/${EXE_NAME}"
}

_install_payload() {
    _decompress_payload /tmp

    mv ${EXEC_PATH} $1
    EXEC_PATH=$1
}

_exec_payload() {
    _install_payload "/tmp/payload"

    exec ${EXEC_PATH} $@
}

# do not allow shell script to execute into the payload
exit 1
__PAYLOAD__
