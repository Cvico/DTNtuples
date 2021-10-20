echo "${@:2}"
root -b << EOF
.x plotAll.C("$1", "${@:2}");
EOF
# .x plotCruijff.C("$1");
