def validar_datos(datos):
    """
    Проверяет логические несоответствия в введённых данных.
    Возвращает список ошибок, если они есть.
    """
    errores = []

    # Пример 1: Тонус мышц не может быть "Нормальный", если есть сильное ограничение движений
    if datos.get("tono_muscular") == "Normal" and datos.get("movilizacion") == "Restricción severa":
        errores.append("El tono muscular no puede ser 'Normal' si la movilización es 'Restricción severa'.")

    # Пример 2: Если "Paso y trote" нормальный, не должно быть значительной боли в позвоночнике
    if datos.get("paso_trote") == "Normal" and datos.get("dolor_columna") == "Dolor severo":
        errores.append("El paso y trote no puede ser 'Normal' si hay dolor severo en la columna.")

    # Пример 3: При "Restricción severa" в тазобедренных суставах, координация должна быть нарушена
    if datos.get("movilizacion") == "Restricción severa" and datos.get("paso_trote") == "Normal":
        errores.append("Si hay 'Restricción severa' en la movilización, el paso y trote no puede ser 'Normal'.")

    # Пример 4: Если "Elevación significativa de cadera" отмечена, не может быть нормальной осанки
    if datos.get("circulos") == "Elevación significativa" and datos.get("postura") == "Normal":
        errores.append("La postura no puede ser 'Normal' si hay 'Elevación significativa de cadera'.")

    # Пример 5: Если "Saltos de conejo" отмечены, мобилизация не может быть полной
    if datos.get("saltos_conejo") == "Sí" and datos.get("movilizacion") == "Normal":
        errores.append("La movilización no puede ser 'Normal' si se detectan 'Saltos de conejo'.")

    # Пример 6: Если зона боли "Lumbar", но движения "Normal", это противоречие
    if datos.get("zona_columna") == "Lumbar" and datos.get("dolor_columna") == "Dolor severo" and datos.get("movilizacion") == "Normal":
        errores.append("Dolor severo en la zona lumbar no puede coincidir con una movilización completamente normal.")

    return errores
  
