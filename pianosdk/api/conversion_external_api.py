from datetime import datetime
from io import StringIO
from typing import TextIO, Dict, List, Union

from pianosdk.api_response import ApiResponse
from pianosdk.base_api import BaseApi
from pianosdk.configuration import Configuration
from pianosdk.httpwrap import HttpCallBack
from pianosdk.utils import _json_deserialize, _encode_parameter
from pianosdk.anon.models.term_conversion import TermConversion


class ConversionExternalApi(BaseApi):
    def __init__(self, config: Configuration, http_callback: HttpCallBack = None) -> None:
        super().__init__(config, http_callback)

    def external_verified_create(self, aid: str, term_id: str, fields: str, user_token: str = None, user_provider: str = None, user_ref: str = None, tracking_id: str = None, custom_params: str = None, browser_id: str = None, page_title: str = None, url: str = None, referer: str = None, content_author: str = None, content_created: str = None, content_section: str = None, content_type: str = None, tags: List[str] = None, previous_user_segments: str = None, cookie_consents: str = None) -> ApiResponse[TermConversion]:
        _url_path = '/api/v3/conversion/external/create'
        _query_url = self.config.get_base_url() + _url_path
        _query_parameters = {

        }

        _headers = {
            'api_token': self.config.api_token,
            'Accept': 'application/json'
        }

        _parameters = {
            'aid': _encode_parameter(aid),
            'term_id': _encode_parameter(term_id),
            'fields': _encode_parameter(fields),
            'user_token': _encode_parameter(user_token),
            'user_provider': _encode_parameter(user_provider),
            'user_ref': _encode_parameter(user_ref),
            'tracking_id': _encode_parameter(tracking_id),
            'custom_params': _encode_parameter(custom_params),
            'browser_id': _encode_parameter(browser_id),
            'page_title': _encode_parameter(page_title),
            'url': _encode_parameter(url),
            'referer': _encode_parameter(referer),
            'content_author': _encode_parameter(content_author),
            'content_created': _encode_parameter(content_created),
            'content_section': _encode_parameter(content_section),
            'content_type': _encode_parameter(content_type),
            'tags': _encode_parameter(tags),
            'previous_user_segments': _encode_parameter(previous_user_segments),
            'cookie_consents': _encode_parameter(cookie_consents)
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
        _result = _json_deserialize(_response, TermConversion)
        return _result

