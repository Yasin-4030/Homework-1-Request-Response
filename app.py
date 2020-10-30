

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def user():
    return "Penguins are cute!"

@app.route('/horse')
def user2():
    return "Horses remind me of my childhood,"
# ------------------------------------------------------------
@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

# ------------------------------------------------------------

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'
# ------------------------------------------------------------

@app.route('/madlibs/<adjective>/<noun>')
def any_word(adjective, noun):
    return f'What is the different between a {adjective} Shark and a lazy {noun}?...{noun} is lazy!'

# -------------------------------------------------------------

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    
    result = int(number1) * int(number2)
    return f'{number1} times {number2} is {result}'
# ------------------------------------------------------------

# @app.route('/sayntimes/<word>/<n>')
# def sayntimes(word,n):
#     for i in range(n):
#         return word


if __name__ == '__main__':
    app.run(debug=True)
