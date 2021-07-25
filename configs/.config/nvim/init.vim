let mapleader=" "

"call plug#begin('~/.local/share/nvim/plugged')
"Plug 'junegunn/goyo.vim'
"call plug#end()

"file type plug-in for file browsing
filetype plugin on
set path+=**
set wildmode=longest,list,full
"system wide clipboard
set clipboard+=unnamedplus
"to stop indenting when pasting with the mouse
set pastetoggle=<F5>
"don't need to save to change a buffer
set hidden
set incsearch
set scrolloff=8
set textwidth=83
set sidescrolloff=999
set scrolloff=999

"programming rules
syntax on
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent
set cindent
"remove auto comment
autocmd Filetype * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
set number

"status line
set laststatus=2
"modified flag, char count, file percent, file path
set statusline=%=%m\ %c\ %P\ %f

"changing the highlight colour
hi Visual cterm=bold ctermbg=darkgrey ctermfg=black
hi MatchParen cterm=bold ctermbg=none ctermfg=red
hi statusline ctermbg=white ctermfg=black
hi SpellBad cterm=bold ctermbg=darkgrey ctermfg=black
set nohlsearch

inoremap jj <Esc>
nnoremap ZW :w<CR>
map <F6> :setlocal spell!<CR>

iab #b /***********************************************************************************
iab #e ***********************************************************************************/
iab com /*<CR><CR>*/<Up>
abbr forl for (int i = 0; i < ; ++i) {<esc>7hi

"check file in shellcheck
map <leader>s :w <bar> :bel 10sp <bar> !clear && shellcheck %<CR>
map <leader>r :w <bar> :bel 10sp <bar> :term gcc % && ./a.out<CR>i
