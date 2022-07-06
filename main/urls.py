from django.urls import path
from main import views

urlpatterns = []

urlvsview = {
    'urls_signup': 'views_form_signup',
    'urls_signin': 'views_form_signin',
    'urls_logout': 'views_form_logout',
    'urls_freelancer': 'views_form_freelancer',
    'urls_company': 'views_form_post_a_company',
    'urls_job': 'views_form_post_a_job',
    'urls_job_proposals': 'views_form_job_proposals',
    'urls_job_offer': 'views_form_job_offer',
    'urls_download_cv': 'views_download_cv',

    '': 'views_index',
    'index': 'views_index',
    'freelancers-search-companies': 'views_freelancers_search_companies',
    'freelancers-browse-jobs': 'views_freelancers_browse_jobs',
    'freelancers-job-proposals': 'views_freelancers_job_proposals',
    'freelancers-job-offers': 'views_freelancers_job_offers',
    'employers-search-freelancers': 'views_employers_search_freelancers',
    'employers-post-a-company': 'views_employers_post_a_company',
    'employers-post-a-job': 'views_employers_post_a_job',
    'employers-manage-jobs': 'views_employers_manage_jobs',
    'employers-manage-candidates': 'views_employers_manage_candidates',
    'single-company-profile': 'views_single_company_profile',
    'single-freelancer-profile': 'views_single_freelancer_profile',
    'single-job-page': 'views_single_job_page',
    'account-settings': 'views_account_settings',
    'about-us': 'views_about_us',
    '404': 'views_404'
}

for key, value in urlvsview.items():
    pattern = path(key, getattr(views, value), name=value)
    urlpatterns.append(pattern)
