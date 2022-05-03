from datetime import date, datetime
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['post', 'get'])
def index_page():
    message = ''
    if request.method == 'POST':
        input = request.form.get('input')
        date_object = datetime.strptime(input, "%d/%m/%Y %H:%M")
        date_ordinal = date_object.toordinal()
        year = date_object.year
        week = ((date_ordinal - _week1_start_ordinal(year)) // 7) + 1
        if date_ordinal < _week1_start_ordinal(year):
            return render_template('index.html', message="Введие дату после 1 января 2019го года")
        return render_template('index.html', message=week)
    return render_template('index.html')


def _week1_start_ordinal(year):
    jan1 = date(2019, 1, 1)
    jan1_ordinal = jan1.toordinal()
    jan1_weekday = jan1.weekday()
    week1_start_ordinal = jan1_ordinal - ((jan1_weekday + 1) % 7)
    return week1_start_ordinal


if __name__ == '__main__':
     app.run(debug=True)

