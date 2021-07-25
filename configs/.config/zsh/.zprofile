# Get aliases and functions
. "$ZDOTDIR/.zshrc"

if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then
  exec sx
fi
