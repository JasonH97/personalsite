from flask import Flask, render_template, url_for
# export FLASK_APP=flaskblog.py -> point flask to main file
# export FLASK_DEBUG=1 -> enable debug mode
app = Flask(__name__)


# TODO: store in db and return content from function call
quotes = [
    {
        'author': 'St. Isaac the Syrian',
        'content' : '"Let this always be the aim of your conduct: to be courteous and respectful to all."'
    },
    {
        'author': 'Elder Thaddeus of Vitovnica',
        'content': '"If we ourselves do not learn humility, God will not stop humbling us"'
    },
    {
        'author': 'Elder Joseph the Hesychast',
        'content': '"...know who you are in truth, and not who you imagine you are. With this knowledge you become the wisest man."'
    },
    {
        'author': 'Bishop Irenei Steenberg',
        'content': '"...obedience is the highest virtue; yet it is also the most basic and the most foundational for all spiritual endeavor."'
    },
]


games = [
    {
     'title': 'Battlefield 3 & 4',
     'platform': 'PC'
    },
    {
     'title': 'Command and Conquer 3',
     'platform': 'PC'
    },
    {
     'title': 'Crash Bandicoot 2: Cortex Strikes Back',
     'platform': 'PSX'
    },
    {
     'title': 'Crash Team Racing',
     'platform': 'PSX'
    },
    {
     'title': 'F-Zero GX',
     'platform': 'GC'
    },
    {
     'title': 'Final Fantasy XII',
     'platform': 'PS2'
    },
    {
     'title': 'Metal Gear Solid 4: Guns of the Patriots',
     'platform': 'PS3'
    },
    {
     'title': 'Pokemon: Emerald Version',
     'platform': 'GBA'
    },
    {
     'title': 'Spyro 2: Ripto\'s Rage',
     'platform': 'PSX'
    },
    {
     'title': 'The Elder Scrolls V: Skyrim',
     'platform': 'PC'
    },
    {
     'title': 'The Legend of Zelda: A Link to the Past',
     'platform': 'SNES'
    },
    {
     'title': 'Yakuza 0',
     'platform': 'PC'
    },
]

articles = [ # TODO: incorporate links to relevant pages like i2p and qutebrowser
    "Removing All Social Media and Embracing RSS",
    "Ditching My Mouse and Adopting a 99% Keyboard-Driven Workflow",
    "Writing Highly-Customized Configs for bash, neovim, and qutebrowser",
    "Podcasts, Warframe, and The Price is Right",
    "Getting Into i2p and Why You Should too",
    "Why I Choose Free/Libre Software",
    "Living Without Google",
    "How I Made my Browser (and Anything Else I Want) Transparent",
]

books = [ # TODO: add designation and corresponding logic
    {
        'name': '(Currently Reading) Clean Code',
        'author': 'Robert Cecil Martin',
        'link': 'https://www.goodreads.com/en/book/show/3735293'
    },
    {
        'name': '(Wishlist) Two Paths: Orthodoxy & Catholicism',
        'author': 'Michael Whelton',
        'link': 'https://www.goodreads.com/en/book/show/56325916'
    },
]

@app.route('/') # homepage
@app.route('/home') # homepage (alt path)
def home():
    html = render_template('home.html',
                           quotes=quotes,
                           games=games,
                           articles=articles,
                           books=books
    )
    return html

if __name__ == '__main__': # only true when running script directly
    app.run(debug=True)

