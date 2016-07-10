class Website(object):
    def __init__(self):
        self.title = 'Robot Parts Manager'

def site_data(request):
    site = Website()
    data = {
        'site': site
    }
    return data
