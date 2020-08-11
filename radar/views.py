from django.shortcuts import render, get_object_or_404, reverse
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect
from .models import College, CollegeDetail
import json, time


def timer(func):  #  计时装饰器
    def wrapper(*args):
        time_start = time.time()
        res = func(*args)
        time_end = time.time()
        print('耗时：{} 秒'.format(round(time_end - time_start, 5)))
        return res
    return wrapper
# Create your views here.

def school_list(request):  #  全学校列表页
    data = College.objects.values('college_name', 'id')
    if not data:
        raise Http404
    else:
        return render(request, 'radar/school_list.html', {'data': data})

def detail(request, pk):  #  详情页，雷达图
    return render(request, 'radar/radar_pic.html', {'pk': pk})

def ajax_detail(request):  #  学校详情json接口
    data = get_object_or_404(College, id=request.GET['pk'])
    college_name = data.college_name
    detail = data.collegedetail_set.filter(year='latest').first()
    context = {
        'detail': [{
            'college_name': college_name,
            'student_count': detail.student_count,
            'full_time': detail.full_time,
            'part_time': detail.part_time}],
        }
    return JsonResponse(context)

@timer
def ajax_search(request):  #  搜索框学校名json接口
    keywords = request.GET['keywords']
    result = College.objects.filter(college_name__icontains=keywords).values('college_name', 'id')[:5]
    if not result:
        raise Http404
    else:
        result = result[:]  #  QuerySet -> List
        return JsonResponse(result, safe=False)

def Home(request):  #  主页重定向
    return HttpResponseRedirect(reverse('radar:school_list'))

@timer
def ajax_compare(request):
    c = [request.GET['c1'], request.GET['c2']]
    context = {
        'detail': []
    }
    for i in c:
        data = get_object_or_404(CollegeDetail, college_name=i, year='latest')
        res = {
            'college_name': i,
            'student_count': data.student_count,
            'full_time': data.full_time,
            'part_time': data.part_time,
            'acceptance_rate': data.acceptance_rate
        }
        context['detail'].append(res)
    return JsonResponse(context)