from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse, Http404, HttpResponse
from .models import College, CollegeDetail
import json

# Create your views here.

def school_list(request):
    data = College.objects.values('college_name', 'id')
    if not data:
        raise Http404
    else:
        return render(request, 'radar/school_list.html', {'data': data})

def detail(request, pk):
    return render(request, 'radar/radar_pic.html', {'pk': pk})

def ajax_detail(request, pk):
    data = College.objects.filter(id=pk).first()  #  id=pk的学校detail信息，类型models，年份为latest
    college_name = data.college_name
    detail = data.collegedetail_set.filter(year='latest').first()
    context = {
        'college_name': college_name,
        'student_count': detail.student_count,
        'full_time': detail.full_time,
        'part_time': detail.part_time
    }
    return JsonResponse(context)