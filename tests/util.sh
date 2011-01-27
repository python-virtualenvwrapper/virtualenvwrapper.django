
load_virtualenvwrapper () {
    if [ ! -z "$VIRTUAL_ENV" ]
    then
        venvw="$VIRTUAL_ENV/bin/virtualenvwrapper.sh"
        export PYTHONPATH="$VIRTUAL_ENV/lib/python*/site-packages"
    else
        venvw=$(which virtualenvwrapper.sh)
    fi
    echo "Loading $venvw"
    source $venvw
}
