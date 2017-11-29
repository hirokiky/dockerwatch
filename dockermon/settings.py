import json
import os


BASE_SETTINGS = {
    'DOCKER_API_VERSION': '',
    'AWS_REGION_NAME': '',
    'AWS_ACCESS_KEY_ID': '',
    'AWS_SECRET_ACCESS_KEY': '',
    'AWS_ASG_NAME': ''
}


_settings = BASE_SETTINGS.copy()


def settings():
    return _settings


def initial_settings(settings_path=None):
    global _settings

    if not settings_path or not os.path.exists(settings_path):
        return

    with open(settings_path) as f:
        data = json.load(f)

    _settings.update(data)
