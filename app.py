from flask import Flask, render_template, request, redirect
from sql import create_clients_table, insert_client  # імпортуємо функції роботи з БД

app = Flask(__name__, static_folder='css')

# Створюємо таблицю клієнтів при запуску сервера
create_clients_table()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/index.html')
def home_():
    return render_template('index.html')
@app.route('/course.html', methods=['GET', 'POST'])
def course():
    if request.method == 'POST':
        posluha = request.form.get('posluha')
        marka = request.form.get('marka')
        city = request.form.get('city')
        time = request.form.get('time')

        # збереження у базу
        if posluha and marka and city and time:
            insert_client(posluha, marka, city, time)

        return redirect('/course.html')  # або показати повідомлення про успішну відправку

    return render_template('course.html')

if __name__ == '__main__':
    app.run(debug=True)
