from django.http import HttpResponse

def html(request):
    # str = '<html>' \
    # '<html>'

    str = """
<html>
    <head>

    </head>

    <body>
        My website
    </body>
</html>
    """
    return HttpResponse(str)
