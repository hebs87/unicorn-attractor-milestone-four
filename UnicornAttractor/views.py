from django.shortcuts import render


def customhandler404(request, exception, template_name='errors/error_404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response


def customhandler500(request, exception, template_name='errors/error_500.html'):
    response = render(request, template_name)
    response.status_code = 500
    return response
