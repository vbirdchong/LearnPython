# -*- coding: utf-8 -*-
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = "http://10.144.1.10:8080"