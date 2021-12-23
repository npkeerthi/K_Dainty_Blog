from flask import Flask,render_template
import requests
posts=requests.get(url="https://api.npoint.io/7a6f2405a54f028b5b54").json()

app = Flask(__name__)
print(posts)
@app.route('/')
def get_all_post():
    return render_template("index.html",all_posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def showpost(index):
    req_post=None
    for bpost in posts:
        if bpost["id"]==index:
            req_post=bpost
    return render_template("post.html",postt=req_post)

if __name__ == '__main__':
    app.run(debug=True)

