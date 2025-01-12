from flask import Flask, render_template, request, redirect, url_for

# Инициализация Flask-приложения
app = Flask(__name__)

# Импорт необходимых функций из других файлов
from validacion import validar_datos
from diagnostico import generar_hipotesis
from recomendaciones import generar_recomendaciones

@app.route('/')
def index():
    """Главная страница"""
    return render_template('index.html')

@app.route('/exploracion_funcional')
def exploracion_funcional():
    """Начальная страница для выбора типа осмотра"""
    return render_template('exploracion_funcional.html')

# Остальная часть кода (ваш пример) остаётся без изменений
@app.route('/fisica', methods=['GET', 'POST'])
def fisica():
    if request.method == 'POST':
        datos = request.form.to_dict()
        errores = validar_datos(datos)
        if errores:
            return render_template('form_fisica.html', errores=errores)
        return redirect(url_for('dinamica', **datos))
    return render_template('form_fisica.html')

@app.route('/dinamica', methods=['GET', 'POST'])
def dinamica():
    if request.method == 'POST':
        datos_dinamica = request.form.to_dict()
        errores = validar_datos(datos_dinamica)
        if errores:
            return render_template('form_dinamica.html', errores=errores)
        return redirect(url_for('columna', **datos_dinamica))
    return render_template('form_dinamica.html')

@app.route('/columna', methods=['GET', 'POST'])
def columna():
    if request.method == 'POST':
        datos_columna = request.form.to_dict()
        errores = validar_datos(datos_columna)
        if errores:
            return render_template('form_columna.html', errores=errores)
        hipotesis = generar_hipotesis(datos_columna)
        recomendaciones = generar_recomendaciones(datos_columna)
        return render_template('resultados.html', hipotesis=hipotesis, recomendaciones=recomendaciones)
    return render_template('form_columna.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
