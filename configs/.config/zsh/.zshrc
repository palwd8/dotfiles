# Git stuff
precmd () { vcs_info }
autoload -Uz vcs_info
zstyle ':vcs_info:*' enable git
zstyle ':vcs_info:git:*' formats '%b '

# Set up the prompt (with git branch name)
setopt PROMPT_SUBST
PROMPT='%B%F{blue}${vcs_info_msg_0_}%F{yellow}%2~%F{red} %# %f%b'

fpath=($ZDOTDIR $fpath)

# Zshoptions
setopt notify nomatch 
stty stop undef # Disable ctrl-s to freeze terminal
zle_highlight=('paste:none')

# Navigation
autoload -Uz bd; bd
setopt autocd autopushd pushdignoredups pushdsilent

# Vi mode
bindkey -v
export KEYTIMEOUT=1
bindkey '^j' vi-cmd-mode
bindkey '^?' backward-delete-char
autoload -Uz edit-command-line; zle -N edit-command-line
bindkey '^f' edit-command-line

autoload -Uz vimcursor
vimcursor

# Completions
. "$ZDOTDIR/completions"

# Source aliases
. "$ZDOTDIR/aliases"

# Fzf
source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh

# Plugins
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
