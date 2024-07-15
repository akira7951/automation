from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.id.models.custom_field_definition_dto import CustomFieldDefinitionDto
from typing import List
from pianosdk.id.models.logout_response import LogoutResponse
from pianosdk.id.models.token_response import TokenResponse


class PublisherApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def create_or_update_custom_fields(self, aid: str, api_token: str, global_validation: bool = None, body: List[CustomFieldDefinitionDto] = None, authorization: str = None) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/publisher/customField'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'api_token': _encode_parameter(api_token),
            'global_validation': _encode_parameter(global_validation)
        }

        _headers = {
            'Authorization': authorization,
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {

        }

        _body = body and body.dict()
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

    def custom_form_submit(self, aid: str, uid: str, custom_fields: str, form_id: str = None, authorization: str = None) -> ApiResponse[Dict]:
        _url_path = '/id/api/v1/publisher/form'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'uid': _encode_parameter(uid),
            'custom_fields': _encode_parameter(custom_fields),
            'form_id': _encode_parameter(form_id)
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

    def login(self, aid: str, email: str, api_token: str, password: str = None, authorization: str = None, remember: bool = None) -> ApiResponse[TokenResponse]:
        _url_path = '/id/api/v1/publisher/login'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'email': _encode_parameter(email),
            'password': _encode_parameter(password),
            'api_token': _encode_parameter(api_token),
            'remember': _encode_parameter(remember)
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
        _result = _json_deserialize(_response, TokenResponse)
        return _result

    def logout(self, aid: str, token: str, authorization: str = None) -> ApiResponse[LogoutResponse]:
        _url_path = '/id/api/v1/publisher/logout'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'token': _encode_parameter(token)
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
        _result = _json_deserialize(_response, LogoutResponse)
        return _result

    def register(self, aid: str, email: str, first_name: str, last_name: str, password: str, consents: str, custom_fields: str, is_passwordless: bool, is_magic_link_sent: bool, form_id: str = None, is_confirmed_email: bool = None, authorization: str = None) -> ApiResponse[TokenResponse]:
        _url_path = '/id/api/v1/publisher/register'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {
            'aid': _encode_parameter(aid),
            'email': _encode_parameter(email),
            'first_name': _encode_parameter(first_name),
            'last_name': _encode_parameter(last_name),
            'password': _encode_parameter(password),
            'consents': _encode_parameter(consents),
            'custom_fields': _encode_parameter(custom_fields),
            'form_id': _encode_parameter(form_id),
            'is_passwordless': _encode_parameter(is_passwordless),
            'is_magic_link_sent': _encode_parameter(is_magic_link_sent),
            'is_confirmed_email': _encode_parameter(is_confirmed_email)
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
        _result = _json_deserialize(_response, TokenResponse)
        return _result

