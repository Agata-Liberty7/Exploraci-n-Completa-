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
  
