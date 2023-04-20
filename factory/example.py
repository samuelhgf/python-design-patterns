#!/usr/bin/env python3

from abc import ABC, abstractmethod

class WebHook(ABC):
    @abstractmethod
    def process_request(self, request_body):
        pass

class WebHookA(WebHook):
    def process_request(self, request_body):
        # logic to process request for WebHook A
        return "WebHook A response"

class WebHookB(WebHook):
    def process_request(self, request_body):
        # logic to process request for WebHook B
        return "WebHook B response"

class WebHookC(WebHook):
    def process_request(self, request_body):
        # logic to process request for WebHook C
        return "WebHook C response"
    
class WebHookFactory:
    WEBHOOKS = {
        "topic_a": WebHookA,
        "topic_b": WebHookB,
        "topic_c": WebHookC,
        # add more mappings as needed
    }

    @staticmethod
    def create_webhook(request_body):
        try:
            webhook_topic = request_body["topic"]
        except KeyError:
            # handle missing or invalid topic
            return None
        
        webhook_class = WebHookFactory.WEBHOOKS.get(webhook_topic, None)
        if not webhook_class:
            # handle unknown topic
            return None
        
        return webhook_class()

request_body = {
    "topic": "topic_a"
}
    
# assume request_body is a string containing the HTTP request body
webhook = WebHookFactory.create_webhook(request_body)
response = webhook.process_request(request_body)
print(response)