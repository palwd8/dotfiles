from qutebrowser.api import interceptor

# Youtube ad blocking
def filter_yt(info: interceptor.Request):
    """Block the given request if necessary."""
    url = info.request_url
    if (
        url.host() == "www.youtube.com"
        and url.path() == "/get_video_info"
        and "&adformat=" in url.query()
    ):
        info.block()


interceptor.register(filter_yt)

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(True)

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set('content.cookies.accept', 'all', 'devtools://*')

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version} Edg/{upstream_browser_version}', 'https://accounts.google.com/*')

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

c.content.blocking.method = 'both'
# Keybindings
config.bind('td', 'config-cycle colors.webpage.darkmode.enabled ;; restart')
config.bind(',ym', 'yank inline [{title}]({url:pretty})')

# Colors
black   = "#0a0e14"
white   = "#fafafa"
gold    = "#e6b450"
red     = "#d96c75"
blue    = "#6994bf"
green   = "#91b362"
darkgrey = "#00010a"
orange  = "#ff8f40"
cyan    = "#95e6cb"
yellow  = "#ffb454"
purple  = "#a37acc"
darkgreen = "#c2d94c"

# Completion Menu
c.colors.completion.category.bg = black
c.colors.completion.category.border.bottom = c.colors.completion.category.border.top = black
c.colors.completion.category.fg = white
c.colors.completion.even.bg = darkgrey
c.colors.completion.odd.bg = darkgrey
c.colors.completion.fg = [blue, green, red]
c.colors.completion.item.selected.bg = c.colors.completion.item.selected.match.fg = black
c.colors.completion.item.selected.border.bottom = c.colors.completion.item.selected.border.top = gold
c.colors.completion.item.selected.bg = gold
c.colors.completion.scrollbar.bg = black
c.colors.completion.scrollbar.fg = white
c.colors.completion.match.fg = white

# Downloads
c.colors.downloads.bar.bg = black
c.colors.downloads.error.bg = red
c.colors.downloads.error.fg = c.colors.downloads.start.fg = c.colors.downloads.stop.fg = black
c.colors.downloads.start.bg = blue
c.colors.downloads.stop.bg = green

# Hints
c.colors.hints.bg = gold
c.colors.hints.fg = black
c.colors.hints.match.fg = white

# Messages
c.colors.messages.error.bg = red
c.colors.messages.error.border = red
c.colors.messages.error.fg = black
c.colors.messages.info.bg = blue
c.colors.messages.info.fg = black
c.colors.messages.warning.bg = c.colors.messages.warning.border = orange
c.colors.messages.warning.fg = black

# Prompts
c.colors.prompts.bg = c.colors.prompts.border = black
c.colors.prompts.selected.bg = gold
c.colors.prompts.selected.fg = black

# Statusbar
c.colors.statusbar.caret.fg = c.colors.statusbar.caret.selection.fg = black
c.colors.statusbar.caret.bg = cyan
c.colors.statusbar.caret.selection.bg = yellow
c.colors.statusbar.command.bg = black
c.colors.statusbar.command.fg = white
c.colors.statusbar.command.private.bg = black
c.colors.statusbar.command.private.fg = white
c.colors.statusbar.insert.bg = blue
c.colors.statusbar.insert.fg = black
c.colors.statusbar.normal.bg = black
c.colors.statusbar.normal.fg = gold
c.colors.statusbar.private.bg = purple
c.colors.statusbar.private.fg = black
c.colors.statusbar.progress.bg = orange
c.colors.statusbar.url.hover.fg = cyan
c.colors.statusbar.url.success.http.fg = darkgreen
c.colors.statusbar.url.success.https.fg = "#86B300"
c.colors.statusbar.url.warn.fg = yellow

# Tabs
c.colors.tabs.bar.bg = black
c.colors.tabs.even.bg = c.colors.tabs.odd.bg = black
c.colors.tabs.pinned.even.bg = c.colors.tabs.pinned.odd.bg = purple
c.colors.tabs.selected.even.bg = c.colors.tabs.selected.odd.bg = black
c.colors.tabs.pinned.selected.odd.bg = c.colors.tabs.pinned.selected.even.bg = purple
c.colors.tabs.pinned.selected.odd.fg = c.colors.tabs.pinned.selected.even.fg = black
c.colors.tabs.even.fg = c.colors.tabs.odd.fg = white
c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg = gold
c.colors.tabs.indicator.error = red
c.colors.tabs.indicator.start = green
c.colors.tabs.indicator.stop = black

# Website
c.colors.webpage.preferred_color_scheme = 'dark'
#c.colors.webpage.darkmode.enabled = True
