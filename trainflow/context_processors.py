def base_template(request):
    if request.user.is_authenticated:
        return {'base_template': 'base_logged_in.html'}
    else:
        return {'base_template': 'base.html'}