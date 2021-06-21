import json
user_response = [
    {
        'select_reason': {
            'type': 'plain_text_input',
            'value': '태스트'
        }
    },
    {
        'datepicker-action': {
            'type': 'datepicker',
            'selected_date': '2021-06-21'
        }           
    },
    {
        'static_select-action': {
            'type': 'static_select',
            'selected_option': {
                'text': {
                    'type': 'plain_text',
                    'text': '정민지',
                    'emoji': True
                },
                'value': 'value-7'
            }
        }
    },
    {
        'select_type': {
            'type': 'radio_buttons',
            'selected_option': {
            'text': {
                    'type': 'plain_text',
                    'text': '연차',
                    'emoji': True
                },
                'value': '3'
            }
        }
    }
]

indexing = []
for response in user_response:
    indexing.append(list(response.keys())[0])

for idx, action_type in enumerate(indexing):
    if action_type == "select_type":
        kind = list(user_response[idx].values())[0]["selected_option"]["text"]["text"]
    elif action_type == "datepicker-action":
        date = list(user_response[idx].values())[0]["selected_date"]
    elif action_type == "static_select-action":
        name = list(user_response[idx].values())[0]["selected_option"]["text"]["text"]
    elif action_type == "select_reason":
        reason = list(user_response[idx].values())[0]["value"]
    else:
        print("pass")

print(name, date, kind, reason)