from flask import Flask, render_template, request, redirect
import random
import string
app = Flask(__name__)

db = {}
print(db)


@app.route('/')
def top():
    p = randomname()
    return render_template('index.html', ttl="OneTime",p=p)

@app.route('/p/<string:p>', methods=['POST', 'GET'])
def done(p):
    print(p)
    if (p in db) and (request.method == 'GET'):
        d = db[p]
        db.pop(p)
        return render_template('source.html', ttl="Get!", d=d)
    else:
        if request.method == 'POST':
            db[p] = request.form['d']
            return render_template('sent.html', ttl="Sent!", p=p)
        else:
            return redirect("/")

def randomname():
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(2)]
    return ''.join(randlst)

if __name__ == "__main__":
    app.run(debug=True)
