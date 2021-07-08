# History
HISTFILE=~/.cache/zsh/histfile
HISTSIZE=10000
SAVEHIST=10000

# Exports
export GOPATH=$HOME/.local/src/go
export CARGO_HOME="$XDG_DATA_HOME"/cargo
export PATH=$PATH:$HOME/.local/bin:$GOPATH/bin
export EDITOR=nvim
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export LESSKEY="$XDG_CONFIG_HOME"/less/lesskey
export LESSHISTFILE="$XDG_CACHE_HOME"/less/history
export STOW_DIR="$HOME/dots"

eval "$(zoxide init zsh)"
export _ZO_DATA_DIR=$XDG_DATA_HOME
export FZF_DEFAULT_OPTS="--layout=reverse --height 60% --color='pointer:red,prompt:red,hl:-1,bg+:blue,gutter:-1,fg+:black'"
