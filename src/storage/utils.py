from datetime import datetime


def generate_filename(extension: str, suffix: str = '') -> str:
    filename = datetime.utcnow().strftime('%d%m%Y_%H%M%S')

    if suffix:
        filename = f'{filename}_{suffix}'

    return f'{filename}.{extension}'
