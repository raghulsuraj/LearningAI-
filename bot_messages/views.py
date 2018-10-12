import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot_messages.utils import detect_intent_with_text_inputs
from bot_messages.validators import Validators
from studyobjects.handlers import *
from user.models import TeamMembership
from utils import prepare_data_for_user


@csrf_exempt
def send_to_dialogflow(request):
    # Send to Dialogflow and receive response

    payload = json.loads(request.body)
    payload = payload["message"]
    prepare_data_for_user(payload)


    team_id = payload["team"]
    user_id = payload["user"]
    text = payload["text"]
    response = detect_intent_with_text_inputs(text, user_id)
    print(response)
    query_response = response["result"]
    if not Validators(query_response).validate():
        # TODO(Sricharan) Find the suitable response
        return HttpResponse()
    try:
        user = TeamMembership.objects.get(platform_user__pk=user_id, team__pk=team_id)
    except ObjectDoesNotExist:
        # TODO(Sricharan) Find the suitable response
        return HttpResponse()
    response_handler_and_action = query_response["action"]
    handler_action_delimiter_index =  response_handler_and_action.find('_')
    handler = response_handler_and_action[:handler_action_delimiter_index]
    action = response_handler_and_action[handler_action_delimiter_index + 1:]
    print("I am here")
    status, response = eval(handler)(query_response["parameters"], user, action)
