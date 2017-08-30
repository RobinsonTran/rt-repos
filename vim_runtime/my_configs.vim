set nocompatible              " be iMproved, required
filetype off                  " required
set nu
set rnu


" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
" Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.

Plugin 'flazz/vim-colorschemes.git'

Plugin 'rafi/awesome-vim-colorschemes.git'

Plugin 'ascenator/L9', {'name': 'newL9'}

Plugin 'kien/ctrlp.vim.git'

Plugin 'scrooloose/nerdtree.git' 

Plugin 'Lokaltog/vim-powerline.git'
set laststatus=2   " Always show the statusline
set encoding=utf-8 " Necessary to show Unicode glyphs
let g:Powerline_symbols = 'unicode'
let g:Powerline_colorscheme = 'solarized256'

 Plugin 'Valloric/YouCompleteMe.git'

"let g:ycm_autoclose_preview_window_after_completion=1
"map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
let g:ycm_server_python_interpreter = '/usr/local/Cellar/python3/3.6.2/bin/python3'

let g:ycm_python_binary_path = '/usr/local/Cellar/python3/3.6.2/bin/python3'
"Uses Python 3 autocomplete


Plugin 'vim-scripts/mru.vim.git'


""""""""""""""""""""""""""""""
" => MRU plugin
""""""""""""""""""""""""""""""
let MRU_Max_Entries = 400
map <leader>f :MRU<CR>


Plugin 'nathanaelkane/vim-indent-guides.git'

let g:indent_guides_enable_on_vim_startup = 1
"Toggles Indent Guides

let g:indent_guides_color_change_percent = 1
let g:indent_guides_auto_colors = 0
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  guibg=purple ctermbg=500
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven guibg=cyan ctermbg=500
"Colorscheme for indent guides


Plugin 'MattesGroeger/vim-bookmarks'
    let mapleader = ","
nmap <Leader><Leader> <Plug>BookmarkToggle
nmap <Leader>i <Plug>BookmarkAnnotate
nmap <Leader>a <Plug>BookmarkShowAll
nmap <Leader>j <Plug>BookmarkNext
nmap <Leader>k <Plug>BookmarkPrev
nmap <Leader>c <Plug>BookmarkClear
nmap <Leader>x <Plug>BookmarkClearAll

  " these will also work with a [count] prefix
nmap <Leader>kk <Plug>BookmarkMoveUp
nmap <Leader>jj <Plug>BookmarkMoveDown
nmap <Leader>g <Plug>BookmarkMoveToLine


"To prevent any default mappings from being created (default: 0):

let g:bookmark_no_default_key_mappings = 1

Plugin 'Syntastic'

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Syntastic (syntax checker)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Python
let g:syntastic_python_checkers=['pyflakes']

" Javascript
let g:syntastic_javascript_checkers = ['jshint']

" Go
let g:syntastic_auto_loc_list = 1
let g:syntastic_go_checkers = ['go', 'golint', 'errcheck']

" Custom CoffeeScript SyntasticCheck
func! SyntasticCheckCoffeescript()
    let l:filename = substitute(expand("%:p"), '\(\w\+\)\.coffee', '.coffee.\1.js', '')
    execute "tabedit " . l:filename
    execute "SyntasticCheck"
    execute "Errors"
endfunc
nnoremap <silent> <leader>c :call SyntasticCheckCoffeescript()<cr>


Plugin 'repeat.vim'

silent! call repeat#set("\<Plug>MyWonderfulMap", v:count)

Plugin '/usr/bin/python3tpope/vim-surround.git'

Plugin 'tpope/vim-commentary.git'



"All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line


"source ~/.vim_runtime/my_configs.vim
