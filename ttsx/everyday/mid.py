
class Mid:
    def process_request(self,request):
        if request.path not in [
                    '/user/register/',
                    '/user/register_handle/',
                    '/user/register_valid/',
                    '/user/login/',
                    '/user/login_handle/',
                    '/user/logout/'
        ]:
            request.session['url_path'] = request.get_full_path()
