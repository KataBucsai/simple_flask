from flask import Flask, render_template, request, redirect

app = Flask(__name__)

get_counter = 0
post_counter = 0
delete_counter = 0
put_counter = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/request-counter')
def get_request_counter():
    global get_counter
    get_counter += 1
    print(get_counter)
    return redirect('/')


@app.route('/request-counter', methods=['POST'])
def post_request_counter():
    global post_counter
    post_counter += 1
    print(post_counter)
    return redirect('/')



if __name__ == '__main__':
    app.run()