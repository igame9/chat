import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message


@csrf_exempt
def index(request):
    if request.method == "GET":
        return render(request, "index.html")

    if request.method == "POST":
        data = request.body.decode('utf-8')
        jsonData = json.loads(data)
        name = jsonData["name"]
        message = jsonData["message"]
        if name == "" or message == "":
            pass

        objectMessage = Message(name=name, message=message)
        objectMessage.save()

        nameMsg = Message.objects.all().values_list("name", flat=True)[0:10]
        # flat = сообщения без скобок и прочего
        msg = Message.objects.all().values_list("message", flat=True)[0:10]
        listWithNameData = []
        listWithMessageData = []

        for name in nameMsg:
            listWithNameData.append(name)
        for value in msg:
            listWithMessageData.append(value)

        tupleMsg = tuple(zip(listWithNameData, listWithMessageData))
        # print(json.loads(json.dumps(tupleMsg)))
        return JsonResponse(json.loads(json.dumps(tupleMsg)), safe=False)


def refreshChat(request):
    if request.method == "GET":

        nameMsg = Message.objects.all().values_list("name", flat=True)[0:10]
        msg = Message.objects.all().values_list("message", flat=True)[0:10]

        listWithNameData = []
        listWithMessageData = []

        for name in nameMsg:
            listWithNameData.append(name)
        for value in msg:
            listWithMessageData.append(value)

        tupleMsg = tuple(zip(listWithNameData, listWithMessageData))
        # print(tupleMsg)
        return JsonResponse(json.loads(json.dumps(tupleMsg)), safe=False)


def warning(request, any):
    return HttpResponse("Нету урла")


def members(request):
    return HttpResponse("Список участников")
