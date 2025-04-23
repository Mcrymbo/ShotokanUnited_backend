from django.shortcuts import render, get_object_or_404
from .knowledge_base.system_prompts import SHOTOKAN_PROMPT
from .knowledge_checker import check_knowledge_base
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
from .signals import create_whatsapp_share_link
from .models import Event

# Create your views here.
def index(request):
    return HttpResponse('This is an introduction page')

def register_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'events/register.html', {'event': event})

@csrf_exempt
def chat_with_deepseek(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            # Layer 1: Check structured knowledge base
            kb_response = check_knowledge_base(user_message)
            if kb_response:
                return JsonResponse({'response': kb_response, 'source': 'knowledge_base'})

            # Layer 2: Use AI with strict prompt
            messages = [
                {"role": "system", "content": SHOTOKAN_PROMPT},
                *data.get('history', []),
                {"role": "user", "content": user_message}
            ]

            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}"},
                json={
                    "model": "microsoft/mai-ds-r1:free",
                    "messages": messages,
                    "temperature": 0.5,  # Lower for more precise answers
                    "max_tokens": 300    # Enforce conciseness
                }
            )

            if response.status_code == 200:
                return JsonResponse({
                    'response': response.json()['choices'][0]['message']['content'],
                    'source': 'ai_model'
                })
            return JsonResponse({'error': 'API request failed'}, status=500)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid method'}, status=400)