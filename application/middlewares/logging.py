import json
import logging

import requests
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from settings.environment_variables import settings


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response: Response = await call_next(request)
        except Exception as e:
            if not settings.DEBUG:
                send_slack_message(str(e))
            logging.error(e._errors)
        return response


def send_slack_message(error_msg: str):
    alarm_emoji = ":rotating_light:"
    text = alarm_emoji + error_msg
    data = json.dumps(
        {
            "attachments": [{"color": "#e01d5a", "text": text}],
        }
    )
    headers = {"Content-Type": "application/json"}
    requests.post(url=settings.SLACK_WEBHOOK_URL, data=data, headers=headers)
