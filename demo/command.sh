#!/bin/sh

# init
#pybabel extract -F ./babel.cfg -k lazy_gettext -o ./messages.pot .
#pybabel init -i ./messages.pot -d ./translations -l zh_CN

# after change html templates
#pybabel extract -F ./babel.cfg -k lazy_gettext -o ./messages.pot .
#pybabel update -N -i ./messages.pot -d ./translations

# after translation
pybabel compile -d ./translations
