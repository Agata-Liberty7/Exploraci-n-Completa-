def generar_hipotesis(datos):
    """
    Генерация гипотез на основе введённых данных.
    """
    hipotesis = []

    # Гипотезы на основе физического осмотра
    if datos.get("movilizacion") == "Restricción severa":
        hipotesis.append("Posible artrosis en la articulación afectada.")
    if datos.get("tono_muscular") == "Hipotonía":
        hipotesis.append("Debilidad muscular generalizada en la extremidad afectada.")
    if datos.get("tono_muscular") == "Hipertonía":
        hipotesis.append("Espasmo muscular en la zona afectada.")

    # Гипотезы на основе динамического осмотра
    if datos.get("paso_trote") == "Anormalidad":
        hipotesis.append("Cojera evidente, posible displasia o dolor articular.")
    if datos.get("circulos") == "Elevación significativa":
        hipotesis.append("Displasia de cadera con elevación pélvica.")
    if datos.get("saltos_conejo") == "Sí":
        hipotesis.append("Posible restricción severa en la movilidad de las extremidades posteriores.")

    # Гипотезы на основе осмотра позвоночника
    if datos.get("dolor_columna") == "Dolor severo":
        hipotesis.append("Compresión nerviosa en la zona lumbar.")
    if datos.get("zona_columna") == "Lumbar" and datos.get("dolor_columna") in ["Dolor leve", "Dolor severo"]:
        hipotesis.append("Lumbalgia mecánica, posible sobrecarga muscular.")

    # Добавление общей гипотезы, если данных недостаточно
    if not hipotesis:
        hipotesis.append("Sin hallazgos claros, se recomienda un estudio adicional.")

    return hipotesis
  
