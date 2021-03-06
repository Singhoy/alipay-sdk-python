#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCognitiveOcrIdcardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCognitiveOcrIdcardQueryResponse, self).__init__()
        self._address = None
        self._birth = None
        self._error_content = None
        self._nationality = None
        self._num = None
        self._request_id = None
        self._sex = None
        self._success = None
        self._trace_id = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def error_content(self):
        return self._error_content

    @error_content.setter
    def error_content(self, value):
        self._error_content = value
    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, value):
        self._nationality = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCognitiveOcrIdcardQueryResponse, self).parse_response_content(response_content)
        if 'address' in response:
            self.address = response['address']
        if 'birth' in response:
            self.birth = response['birth']
        if 'error_content' in response:
            self.error_content = response['error_content']
        if 'nationality' in response:
            self.nationality = response['nationality']
        if 'num' in response:
            self.num = response['num']
        if 'request_id' in response:
            self.request_id = response['request_id']
        if 'sex' in response:
            self.sex = response['sex']
        if 'success' in response:
            self.success = response['success']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
