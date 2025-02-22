from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return render_template('profile_page.html', name="Bogodukhov Nikita", bio="Information Security specialis.")

if __name__ == '__main__':
    app.run()
