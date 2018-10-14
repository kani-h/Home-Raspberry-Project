from home_service.config import env_config
import abc
import requests
import json
import sys
import os


class BaseService(metaclass=abc.ABCMeta):
    _headers = None
    _account_id = None
    _account_name = None
    _api_config = None
    _base_url = None

    def __init__(self):
        argv = sys.argv
        env = os.environ.get('PY_ENV')

        if env == 'local' or 'local' in argv:
            cfg = env_config.LocalConfig()
        elif env == 'development' or 'development' in argv:
            cfg = env_config.DevelopmentConfig()
        elif env == 'production' or 'production' in argv:
            cfg = env_config.ProductionConfig()
        else:
            cfg = env_config.DevelopmentConfig()

        self._headers = {}
        self._base_url = cfg.PROTOCOL + '://' + cfg.HOST + ':' + cfg.PORT + cfg.BASE_PATH

    def _requester(self, api_config, params=None, data=None, target=None):
        url = self._base_url + api_config.get('prefix') + api_config.get('url')
        method = api_config.get('method').lower()

        if target is not None:
            url = url.replace(":id", str(target))

        self._headers['Content-Type'] = api_config.get('contentsType')

        call_api = getattr(requests, method)

        response = call_api(url, headers=self._headers, params=params, data=data)

        return Response(response)


class RetrieveService(BaseService):
    def find_one(self, data_id):
        api_config = self._api_config.get('find_one')

        return self._requester(api_config, target=data_id)

    def find(self, page=None, size=None, sort=None):
        api_config = self._api_config.get('find')
        params = {'page': page, 'size': size, 'sort': sort}

        return self._requester(api_config, params=params)


class AlterService(BaseService):
    def create(self, data):
        api_config = self._api_config.get('create')

        return self._requester(api_config, data=json.dumps(data))

    def update(self, data_id, data):
        api_config = self._api_config.get('update')

        return self._requester(api_config, data=json.dumps(data), target=data_id)

    def delete(self, data_id):
        api_config = self._api_config.get('delete')

        return self._requester(api_config, target=data_id)


class Response:
    _status_code = None
    _data = None
    _error = None
    _is_ok = False

    def __init__(self, response):

        # FIXME 정상응답 범위지만, 코드에 따른 세분화 필요.
        self._status_code = response.status_code
        self._is_ok = (200 <= response.status_code < 400)
        if self._is_ok:
            if 200 <= self._status_code <= 201:
                self._data = json.loads(json.dumps(response.json()))
        else:
            self._error = response.text

    def get_data(self):
        if self._is_ok:
            return self._data
        else:
            return None

    def get_error(self):
        return self._error

    def is_ok(self):
        return self._is_ok
