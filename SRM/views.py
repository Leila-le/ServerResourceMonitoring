from django.shortcuts import render
import psutil
from dingtalkchatbot.chatbot import DingtalkChatbot
# Create your views here.


def home(request):
    #获取服务器状态
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent


    #发送钉钉消息
    webhook = 'your_webhook_url_here'
    secret = 'your_secret_here'
    xiaoding = DingtalkChatbot(webhook, secret = secret)
    message = f"CPU usage: {cpu_percent}%\nMemory usage: {memory_percent}%\nDisk usage: {disk_percent}%"
    xiaoding.send_text(msg=message, is_at_all=False)

    return render(request, 'SRM/home.html', {'cpu_percent': cpu_percent, 'memory_percent': memory_percent, 'disk_percent': disk_percent})