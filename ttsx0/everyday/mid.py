
class Mid:
    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.path not in [
                    '/user/register/',
                    '/user/register_handle/',
                    '/user/register_vaild/',
                    '/user/login/',
                    '/user/login_handle/',
                    '/user/logout/'
        ]:
            request.session['url_path'] = request.get_full_path()
