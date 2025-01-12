def generar_recomendaciones(datos):
    """
    Генерация рекомендаций на основе введённых данных и гипотез.
    """
    recomendaciones = []

    # Рекомендации для физического осмотра
    if datos.get("movilizacion") == "Restricción severa":
        recomendaciones.append("Terapia láser 3 veces por semana para reducir la inflamación.")
        recomendaciones.append("Movilización pasiva diaria para mejorar el rango de movimiento.")
    if datos.get("tono_muscular") == "Hipotonía":
        recomendaciones.append("Ejercicios de fortalecimiento muscular 2-3 veces por semana.")
    if datos.get("tono_muscular") == "Hipertonía":
        recomendaciones.append("Terapia de calor para relajar los espasmos musculares.")

    # Рекомендации для динамического осмотра
    if datos.get("paso_trote") == "Anormalidad":
        recomendaciones.append("Ejercicios de equilibrio para corregir la marcha.")
    if datos.get("circulos") == "Elevación significativa":
        recomendaciones.append("Fortalecimiento de los músculos abductores.")
    if datos.get("saltos_conejo") == "Sí":
        recomendaciones.append("Se recomienda terapia acuática para reducir la presión en las articulaciones.")

    # Рекомендации для осмотра позвоночника
    if datos.get("dolor_columna") == "Dolor severo":
        recomendaciones.append("Consulta con un especialista en neurología.")
        recomendaciones.append("Fisioterapia para aliviar la tensión lumbar.")
    if datos.get("zona_columna") == "Lumbar" and datos.get("dolor_columna") == "Dolor leve":
        recomendaciones.append("Estiramientos suaves de la zona lumbar.")

    # Общие рекомендации
    if not recomendaciones:
        recomendaciones.append("Monitoreo continuo sin intervenciones específicas.")

    return recomendaciones
  
