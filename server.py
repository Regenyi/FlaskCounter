from flask import Flask, redirect, render_template

app = Flask(__name__)
counter = 0


@app.route('/')
def index():
    global counter
    return render_template('index.html', counter=counter)


@app.route('/request-counter', methods=['GET'])
def req_counter():
    global counter
    counter += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True,
        # host='0.0.0.1',
        port=5000
    )


# PC tod: setup keys, move down up, setup intellisense
