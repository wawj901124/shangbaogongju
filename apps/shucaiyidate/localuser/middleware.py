from shucaiyidate.forms import guolu_name_id

def simple_middleware(get_response):  #自定义类中间件
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次。
    print('1----django启动了')

    def middleware(request):   #自定义中间键函数
        # 此处编写的代码会在每个请求处理视图前被调用。
        print('2----请求视图前被调用')
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        print('用户的请求ip是', ip)
        print(request.META['USERNAME'])
        response = get_response(request)

        # 此处编写的代码会在每个请求处理视图之后被调用。
        print('3----请求视图后被调用')
        user = request._cached_user
        guolu_name_id = user
        print("中间键中的guolu_name_id：")
        print(guolu_name_id)
        print("请求的用户是",user)
        return response

    return middleware