from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.id.models.token_response_vx_compatible import TokenResponseVxCompatible


class IdentityVxauthApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def authorize(self) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/identity/vxauth/authorize'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {

        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('GET',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response)
        return _result

    def create_cookie_with_aid_and_token(self, authorization: str = None, token: str = None, client_id: str = None, session_cookie: bool = None) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/identity/vxauth/cookie'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'token': _encode_parameter(token),
            'client_id': _encode_parameter(client_id),
            'session_cookie': _encode_parameter(session_cookie)
        }

        _headers = {
            'Authorization': authorization,
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('GET',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response)
        return _result

    def create_cookie_with_aid_and_token_post(self, authorization: str = None, token: str = None, client_id: str = None, session_cookie: bool = None) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/identity/vxauth/cookie'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'token': _encode_parameter(token),
            'client_id': _encode_parameter(client_id),
            'session_cookie': _encode_parameter(session_cookie)
        }

        _headers = {
            'Authorization': authorization,
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('POST',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response)
        return _result

    def refresh_token_or_exchange_code(self, client_id: str = None, refresh_token: str = None, grant_type: str = None, code: str = None, client_secret: str = None, redirect_uri: str = None, code_verifier: str = None) -> ApiResponse[TokenResponseVxCompatible]:
        _url_path = '/id/api/v1/identity/vxauth/token'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {

        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {
            'client_id': _encode_parameter(client_id),
            'refresh_token': _encode_parameter(refresh_token),
            'grant_type': _encode_parameter(grant_type),
            'code': _encode_parameter(code),
            'client_secret': _encode_parameter(client_secret),
            'redirect_uri': _encode_parameter(redirect_uri),
            'code_verifier': _encode_parameter(code_verifier)
        }

        _body = None
        _files = None

        _request = self.config.http_client.build_request('POST',
                                                         _query_url,
                                                         headers=_headers,
                                                         query_parameters=_query_parameters,
                                                         parameters=_parameters,
                                                         json=_body,
                                                         files=_files)
        _response = self._execute_request(_request)
        _result = _json_deserialize(_response, TokenResponseVxCompatible)
        return _result

