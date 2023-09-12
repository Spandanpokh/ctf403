from django.shortcuts import render
from django.http import HttpResponse

def forbidden(request):
    # Check if the X-Forwarded-For header is present
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    
    if forwarded_for:
        # If the header is present, render the success template
        return render(request, 'myapp/success.html')
    else:
        # If the header is not present, return a 403 Forbidden response with links
        response_content = """
        <html>
        <head>
            <title>403 Access Forbidden</title>
        </head>
        <body>
            <h1>403 Access Forbidden</h1>
            <p>Need help to solve this CTF? Contact me here,</p>
            <a href="https://www.facebook.com/spandanpokh/">Facebook</a>
            <a href="https://www.linkedin.com/in/spandanpokh/">LinkedIn</a>
        </body>
        </html>
        """
        return HttpResponse(response_content, status=403)
