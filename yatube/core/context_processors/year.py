import datetime

def year(request):
    """Добавляет переменную с текущим годом."""
    now = datetime.datetime.now()
    return {
        'year': now.year,
    }