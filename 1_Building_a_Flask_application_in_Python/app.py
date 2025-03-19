from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return  "Home"

@app.route("/movie")
def movie():
    html = ("<html><head><title>Movie Page</title></head>"
            "<body><h1>My all-time favorite movie is The Evil Dead!</h1>"
            "<p>The Evil Dead (1981) stands out as a horror classic due to its masterful building of tension,\n"
            " subversion of expectations, and unrelenting pace. Sam Raimi’s self-aware humor, courtesy of his\n"
            " irreverent script and Bruce Campbell’s iconic performance as Ash Williams, adds complexity to the\n"
            " narrative, making it both a cult favorite and influential force in popular culture. By pushing the\n"
            " boundaries of on-screen violence with practical effects and clever editing, The Evil Dead has had\n"
            " a lasting impact on the horror genre, inspiring countless imitators and influencing prominent\n"
            " filmmakers like Eli Roth and Rob Zombie. Its enduring reputation is cemented by its status as an\n"
            " original, bold vision that continues to captivate audiences today.</p></body></html>")
    return html

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
