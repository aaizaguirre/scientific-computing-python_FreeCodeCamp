"""
Time Calculator Project
Crea una función "add_time" que toma una hora de inicio, 
una duración y un día de la semana (opcional) 
y devuelve la hora final después de sumar la duración al tiempo de inicio.
"""
def add_time(start:str, duration: str, day:str=None) -> str:
    """
    Agrega una duración a la hora de inicio en formato de 12 horas.
    Parámetros:
    - start (str): Hora de inicio en formato "HH:MM AM/PM".
    - duration (str): Duración en formato "HH:MM".
    - day (str, opcional): Día de la semana.
    Devuelve:
    - str: Hora final en formato "HH:MM AM/PM", 
    con día de la semana y días transcurridos (opcional).
    """
    # Descomposición del tiempo de inicio
    time, period = start.split()
    hour, minute = map(int, time.split(':'))
    # Convertir el tiempo de inicio a formato 24 horas
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0
    # Descomposición de la duración
    duration_hour, duration_minute = map(int, duration.split(':'))
    # Suma de minutos y horas
    end_minute = minute + duration_minute
    end_hour = hour + duration_hour + end_minute // 60
    end_minute = end_minute % 60
    # Cálculo de días transcurridos
    days_later = end_hour // 24
    end_hour %= 24
    # Conversión de vuelta a formato 12 horas
    if end_hour == 0:
        final_hour = 12
        final_period = 'AM'
    elif end_hour < 12:
        final_hour = end_hour
        final_period = 'AM'
    elif end_hour == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = end_hour - 12
        final_period = 'PM'
    # Construcción del tiempo final
    new_time = f"{final_hour}:{end_minute:02d} {final_period}"
    # Cálculo del día de la semana si se proporciona
    if day:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_index = days.index(day.capitalize())
        final_day = days[(start_index + days_later) % 7]
        new_time += f", {final_day}"
    # Añadir información sobre días transcurridos
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    return new_time
