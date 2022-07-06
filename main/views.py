from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
from main import models
from datetime import date
import os


keyname_freelancer = ['username', 'emailaddress', 'password', 'freelancer_name_first', 'freelancer_name_last',
                      'freelancer_picture',
                      'freelancer_type', 'freelancer_phone', 'freelancer_salary', 'freelancer_skills',
                      'freelancer_tagline', 'freelancer_tagline', 'freelancer_nationality',
                      'freelancer_description']

keyname_company = ['username', 'company_picture', 'company_username', 'company_name',
                   'company_location', 'company_category', 'company_tagline', 'company_description']

keyname_job = ['username', 'job_picture', 'company_username', 'job_timebegin', 'job_timeend',
               'job_title', 'job_location', 'job_type', 'job_category',
               'job_salary', 'job_description', 'job_postion', 'job_username']

keyname_job_proposals = ['username', 'job_username', 'job_proposals_cv']

keyname_job_offers = ['username', 'job_username', 'job_offers_email']

loginurl = [
    'freelancers-job-proposals',
    'freelancers-job-offers',
    'employers-post-a-company',
    'employers-post-a-job',
    'employers-manage-jobs',
    'employers-manage-candidates',
    'account-settings'
]

commonurl = [
    '',
    'index',
    'freelancers-search-companies',
    'freelancers-browse-jobs',
    'employers-search-freelancers',
    'single-company-profile',
    'single-freelancer-profile',
    'single-job-page',
    'about-us#contact',
    'about-us#privacy_policies',
    'about-us#terms_of_use'
]

logoutfunction = ['views_form_signup', 'views_form_signin']

loginfunction = ['views_form_logout',
                 'views_form_freelancer',
                 'views_form_post_a_company',
                 'views_form_post_a_job',
                 'views_form_job_proposals'
                 'views_freelancers_job_proposals',
                 'views_freelancers_job_offers',
                 'views_employers_post_a_company',
                 'views_employers_post_a_job',
                 'views_employers_manage_jobs',
                 'views_employers_manage_candidates']

commonfunction = ['views_index',
                  'views_about_us',
                  'views_single_company_profile',
                  'views_single_freelancer_profile',
                  'views_single_job_page',
                  'views_freelancers_browse_jobs',
                  'views_freelancers_search_companies',
                  'views_employers_search_freelancers']


class HeadlineClass:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third


def set_session(request, post):
    request.session['username'] = post.username
    request.session['freelancer_picture'] = post.freelancer_picture


def filtering_salary(value):
    value = value.replace('$', '')
    value = value.replace('k', '')
    return value


def save_originalfile(filename, columnname, request):
    if filename not in request.FILES:
        return False
    filename2 = f"main/static/{filename}"
    originalfile = request.FILES[columnname]
    fs = FileSystemStorage()
    fs.delete(filename2)
    fs.save(filename2, originalfile)


def download_cv(path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def views_download_cv(request):
    if request.method == 'POST':
        path = request.POST['download_path']
        download_cv(path)
        urlpre = request.META.get('HTTP_REFERER', '/')
        return redirect(urlpre)


def get_aboulte_url(urlname):
    urlname = os.path.basename(urlname)
    urlname = urlname.split('?')[0]
    return urlname


def get_previous_url(request, functionname):
    login = 'username' in request.session
    check1 = functionname in ['views_form_signup', 'views_form_signin'] and not login
    check2 = functionname in ['views_form_logout'] and login

    urlfst = views_index
    urlsec = request.META.get('HTTP_REFERER', '/')
    urlname = get_aboulte_url(urlsec)
    urlfinal = ''

    if check1:
        urlfinal = urlsec
    if check2 and urlname in commonurl:
        urlfinal = urlsec
    if check2 and urlname in loginurl:
        urlfinal = urlfst

    return urlfinal


def checkmate(request, functionname):
    login = 'username' in request.session
    check1 = functionname in logoutfunction and login
    check2 = functionname in loginfunction and not login

    urlfst = views_index
    urlsec = request.META.get('HTTP_REFERER', '/')
    urlname = get_aboulte_url(urlsec)
    urlfinal = ''

    if check1:
        urlfinal = urlsec
    if check2 and urlname in commonurl:
        urlfinal = urlsec
    if check2 and urlname in loginurl:
        urlfinal = urlfst

    return urlfinal


def views_form_signup(request):
    urlfinal = checkmate(request, 'views_form_signup')
    if urlfinal != '':
        return redirect(urlfinal)

    urlpre = get_previous_url(request, 'views_form_signup')

    if request.method == 'POST':
        if request.POST['password'] != request.POST['repeatpassword']:
            return redirect('index')

        post = models.Models_freelancer()
        post.username = request.POST['username']
        post.emailaddress = request.POST['emailaddress']
        post.password = request.POST['password']
        post.freelancer_picture = 'images/a_freelancer_profile_picture.jpg'
        post.freelancer_type = 'Freelancer'
        post.freelancer_salary = '$5k'

        dontdo = ['username', 'emailaddress', 'password', 'freelancer_picture', 'freelancer_type', 'freelancer_salary']

        for k in keyname_freelancer:
            if k in dontdo:
                continue
            setattr(post, k, '-')
        post.save()

        set_session(request, post)
        return redirect(urlpre)


def views_form_signin(request):
    urlfinal = checkmate(request, 'views_form_signin')
    if urlfinal != '':
        return redirect(urlfinal)

    urlpre = get_previous_url(request, 'views_form_signin')

    if request.method == 'POST':
        post = models.Models_freelancer.objects.get(username=request.POST['username'],
                                                    emailaddress=request.POST['emailaddress'],
                                                    password=request.POST['password'])

        number = models.Models_freelancer.objects.filter(username=request.POST['username'],
                                                         emailaddress=request.POST['emailaddress'],
                                                         password=request.POST['password']).count()
        if number == 1:
            set_session(request, post)
        return redirect(urlpre)


def views_form_logout(request):
    urlfinal = checkmate(request, 'views_form_logout')
    if urlfinal != '':
        return redirect(urlfinal)

    urlpre = get_previous_url(request, 'views_form_logout')
    del request.session['username']
    return redirect(urlpre)


def views_form_freelancer(request):
    urlfinal = checkmate(request, 'views_form_freelancer')
    if urlfinal != '':
        return redirect(urlfinal)

    if request.method == 'POST':
        post = models.Models_freelancer.objects.get(username=request.session['username'])
        c1 = post.emailaddress == request.POST['emailaddress']
        c2 = post.password == request.POST['currentpassword']

        dontdo = ['username', 'password', 'freelancer_salary', 'freelancer_picture']

        if c1 and c2:
            filename = f"images/a_{request.session['username']}_profile_picture.jpg"
            columnname = 'freelancer_picture'
            save_originalfile(filename, columnname, request)
            setattr(post, columnname, filename)

            for k in keyname_freelancer:
                if k in dontdo:
                    continue
                setattr(post, k, request.POST[k])

            post.freelancer_salary = '$' + request.POST['freelancer_salary'] + 'k'
            post.password = request.POST['newpassword']
            post.save()
            set_session(request, post)

        return redirect('views_account_settings')


def views_form_post_a_company(request):
    urlfinal = checkmate(request, 'views_form_post_a_company')
    if urlfinal != '':
        return redirect(urlfinal)

    if request.method == 'POST':
        post = models.Models_company()
        post.username = request.session['username']

        filename = f"images/b_{request.POST['company_username']}_profile_picture.jpg"
        columnname = 'company_picture'
        save_originalfile(filename, columnname, request)
        setattr(post, columnname, filename)

        for k in keyname_company:
            if k == 'username' or k == 'company_picture':
                continue
            setattr(post, k, request.POST[k])
        post.save()

        return redirect(views_employers_post_a_company)


def views_form_post_a_job(request):
    urlfinal = checkmate(request, 'views_form_post_a_job')
    if urlfinal != '':
        return redirect(urlfinal)

    if request.method == 'POST':
        today = date.today()

        post = models.Models_job()

        post.username = request.session['username']
        post.job_timebegin = str(today.strftime("%m/%d/%y"))
        post.job_timeend = str(request.POST['job_timeend'])

        filename = f"images/c_{request.POST['job_username']}_profile_picture.jpg"
        columnname = 'job_picture'
        save_originalfile(filename, columnname, request)
        setattr(post, columnname, filename)

        for k in keyname_job:
            if k == 'username' or k == 'job_picture' or k == 'job_timebegin' or k == 'job_timeend':
                continue
            setattr(post, k, request.POST[k])
        post.save()

        return redirect(views_employers_post_a_job)


def views_form_job_proposals(request):
    urlfinal = checkmate(request, 'views_form_job_proposals')
    if urlfinal != '':
        return redirect(urlfinal)

    if request.method == 'POST':
        post = models.Models_job_proposals()
        post.username = request.session['username']
        post.job_username = request.POST['job_username']

        filename = f"images/f_{request.session['username']}_{post.job_username}_cv.pdf"
        columnname = 'job_proposals_cv'
        save_originalfile(filename, columnname, request)
        setattr(post, columnname, filename)

        post.save()

        urlpre = request.META.get('HTTP_REFERER', '/')
        return redirect(urlpre)


def views_form_job_offer(request):
    urlfinal = checkmate(request, 'views_form_job_offer')
    if urlfinal != '':
        return redirect(urlfinal)

    if request.method == 'POST':
        post = models.Models_job_offers()
        post.username = request.session['username']
        post.job_username = request.POST['job_username']
        post.job_offers_email = request.POST['job_offers_email']
        post.save()

        urlpre = request.META.get('HTTP_REFERER', '/')
        return redirect(urlpre)


def views_freelancers_job_proposals(request):
    urlfinal = checkmate(request, 'views_freelancers_job_proposals')
    if urlfinal != '':
        return redirect(urlfinal)

    headline = HeadlineClass('Job Proposals', 'Employee', 'Job Proposals')
    data_job = []
    data_job_proposals = models.Models_job_proposals.objects.all().filter(username=request.session['username'])
    for i in data_job_proposals:
        post = models.Models_job.objects.get(job_username=i.job_username)
        data_job.append(post)

    context = {'data_job': data_job, 'headline': headline}

    return render(request, 'freelancers-job-proposals.html', context)


def views_freelancers_job_offers(request):
    urlfinal = checkmate(request, 'views_freelancers_job_offers')
    if urlfinal != '':
        return redirect(urlfinal)

    headline = HeadlineClass('Job Offers', 'Employee', 'Job Offers')
    data_job = []
    data_job_offers = models.Models_job_offers.objects.all().filter(username=request.session['username'])
    for i in data_job_offers:
        post = models.Models_job.objects.get(job_username=i.job_username)
        data_job.append(post)

    context = {'data_job': data_job, 'headline': headline}

    return render(request, 'freelancers-job-offers.html', context)


def views_employers_post_a_company(request):
    urlfinal = checkmate(request, 'views_employers_post_a_company')
    if urlfinal != '':
        return redirect(urlfinal)

    headline = HeadlineClass('Post a Company', 'Employers', 'Post a Company')
    data_company_category = models.Models_company_category.objects.all()
    data_company = models.Models_company.objects.all()

    context = {
        'data_company_category': data_company_category,
        'data_company': data_company,
        'headline': headline
    }

    return render(request, 'employers-post-a-company.html', context)


def views_employers_post_a_job(request):
    urlfinal = checkmate(request, 'views_employers_post_a_job')
    if urlfinal != '':
        return redirect(urlfinal)

    headline = HeadlineClass('Post a Job', 'Employers', 'Post a Job')
    data_jobs_company_username = models.Models_company.objects.all()
    data_job_category = models.Models_job_category.objects.all()
    data_job_type = ['Full-Time', 'Part-Time', 'Internship', 'Temporary']
    data_jobs = models.Models_job.objects.all()

    context = {
        'data_jobs_company_username': data_jobs_company_username,
        'data_job_category': data_job_category,
        'data_job_type': data_job_type,
        'data_jobs': data_jobs,
        'headline': headline
    }

    return render(request, 'employers-post-a-job.html', context)


def views_employers_manage_jobs(request):
    urlfinal = checkmate(request, 'views_employers_manage_jobs')
    if urlfinal != '':
        return redirect(urlfinal)

    username = request.session['username']
    headline = HeadlineClass('Manage Jobs', 'Employers', 'Manage Jobs')
    data_manage_jobs = models.Models_job.objects.all().filter(username=username)

    candidate_number = []
    for i in data_manage_jobs:
        number = models.Models_job_proposals.objects.filter(job_username=i.job_username).count()
        candidate_number.append(number)

    zipfile = zip(data_manage_jobs, candidate_number)
    context = {
        'zipfile': zipfile,
        'headline': headline
    }

    return render(request, 'employers-manage-jobs.html', context)


def views_employers_manage_candidates(request):
    urlfinal = checkmate(request, 'views_employers_manage_candidates')
    if urlfinal != '':
        return redirect(urlfinal)

    job_username = request.GET.get('job_username')
    candidate_number = request.GET.get('candidate_number')
    headline = HeadlineClass('Manage Candidates', 'Employers', 'Manage Candidates')
    data_manage_candidates = models.Models_job_proposals.objects.all().filter(job_username=job_username)
    data_manage_candidates_profile = []
    data_manage_candidates_cv = []

    for i in data_manage_candidates:
        post = models.Models_freelancer.objects.get(username=i.username)
        cv = models.Models_job_proposals.objects.all().filter(job_username=job_username, username=i.username)
        data_manage_candidates_profile.append(post)
        data_manage_candidates_cv.append(cv)

    zipfile = zip(data_manage_candidates_profile, data_manage_candidates_cv)

    context = {
        'zipfile': zipfile,
        'candidate_number': candidate_number,
        'headline': headline
    }

    return render(request, 'employers-manage-candidates.html', context)


def views_account_settings(request):
    urlfinal = checkmate(request, 'views_account_settings')
    if urlfinal != '':
        return redirect(urlfinal)

    data_freelancer = models.Models_freelancer.objects.get(username=request.session['username'])
    data_nationality = models.Models_nationality.objects.all()
    data_freelancer_type = ['Freelancer', 'Employer']

    data_freelancer.freelancer_salary = filtering_salary(data_freelancer.freelancer_salary)

    headline = HeadlineClass('Settings', 'Account', 'Settings')

    context = {
        'data_nationality': data_nationality,
        'data_freelancer_type': data_freelancer_type,
        'data_freelancer': data_freelancer,
        'headline': headline
    }

    return render(request, 'account-settings.html', context)


def views_index(request):
    data_freelancer = models.Models_freelancer.objects.all()
    data_company = models.Models_company.objects.all()
    data_job = models.Models_job.objects.all()

    context = {
        'data_freelancer': data_freelancer,
        'data_company': data_company,
        'data_job': data_job
    }

    return render(request, 'index.html', context)


def views_freelancers_search_companies(request):
    headline = HeadlineClass('Search Companies', 'Employees', 'Search Companies')
    data_company = models.Models_company.objects.all()
    context = {'data_company': data_company, 'headline': headline}
    return render(request, 'freelancers-search-companies.html', context)


def views_freelancers_browse_jobs(request):
    headline = HeadlineClass('Browse Jobs', 'Employee', 'Browse Jobs')
    data_job = models.Models_job.objects.all()
    context = {'data_job': data_job, 'headline': headline}
    return render(request, 'freelancers-browse-jobs.html', context)


def views_employers_search_freelancers(request):
    headline = HeadlineClass('Search Employees', 'Employers', 'Search Employees')
    data_freelancer = models.Models_freelancer.objects.all()
    context = {'data_freelancer': data_freelancer, 'headline': headline}
    return render(request, 'employers-search-freelancers.html', context)


def views_single_freelancer_profile(request):
    username = request.GET.get('username')
    data_freelancer_single = models.Models_freelancer.objects.get(username=username)
    freelancer_skills = data_freelancer_single.freelancer_skills
    freelancer_skills = freelancer_skills.split(', ')

    context = {
        'data_freelancer_single': data_freelancer_single,
        'freelancer_skills': freelancer_skills
    }

    return render(request, 'single-freelancer-profile.html', context)


def views_single_company_profile(request):
    company_username = request.GET.get('company_username')
    data_company_single = models.Models_company.objects.get(company_username=company_username)
    context = {'data_company_single': data_company_single}
    return render(request, 'single-company-profile.html', context)


def views_single_job_page(request):
    job_username = request.GET.get('job_username')
    data_job_single = models.Models_job.objects.get(job_username=job_username)
    context = {'data_job_single': data_job_single}
    return render(request, 'single-job-page.html', context)


def views_about_us(request):
    headline = HeadlineClass('Contact', 'About Us', 'Contact')
    context = {'headline': headline}
    return render(request, 'about-us.html', context)


def views_404(request):
    return render(request, '404.html')
