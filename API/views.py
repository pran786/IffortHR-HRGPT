from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import requests
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import openai
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from .services import HRAssistant

hr_assistant = HRAssistant("Knowledgebase.txt")

class HRAssistantView(APIView):
    def post(self, request):
        query = request.data.get('query')
        if not query:
            return Response({"error": "No query provided"}, status=400)
        
        response = hr_assistant.get_response(query)
        return Response({"response": response})


# Create your views here.
def index(request):
    return render(request,'index.html')















