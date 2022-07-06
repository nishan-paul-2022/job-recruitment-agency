import glob
import os
import re


def add_line(path):
    print(path)
    sub = path + '*.html'
    slist = glob.glob(sub)
    print(slist)

    for i in range(len(slist)):
        oname = slist[i]
        print(oname)
        with open(oname, 'r', encoding='utf8') as original:
            data = original.read()
        with open(oname, 'w', encoding='utf8') as modified:
            modified.write("{% load static %}\n" + data)


if __name__ == '__main__':
    # add_line('E:/CODE/PYTHON/done_backend_developing/done_backend_ecommerce/main/templates/')
    print()


# http://127.0.0.1:8000/404 / ax

# http://127.0.0.1:8000/index / ax

# http://127.0.0.1:8000/freelancers-search-companies / ax
# http://127.0.0.1:8000/freelancers-browse-jobs / bx
# http://127.0.0.1:8000/freelancers-job-proposals / bx
# http://127.0.0.1:8000/freelancers-job-offers / bx

# http://127.0.0.1:8000/employers-search-freelancers / bx
# http://127.0.0.1:8000/employers-post-a-job / bx
# http://127.0.0.1:8000/employers-manage-jobs / bx
# http://127.0.0.1:8000/employers-manage-candidates / bx

# http://127.0.0.1:8000/single-company-profile / ax
# http://127.0.0.1:8000/single-freelancer-profile / ax
# http://127.0.0.1:8000/single-job-page / ax

# http://127.0.0.1:8000/account-settings / bx

# http://127.0.0.1:8000/about-us / ax

# http://127.0.0.1:8000/_about_us_contact.html
# http://127.0.0.1:8000/_about_us_privacy_policies.html
# http://127.0.0.1:8000/_about_us_terms_of_use.html

# http://127.0.0.1:8000/_account_settings_my_account.html
# http://127.0.0.1:8000/_account_settings_my_profile.html
# http://127.0.0.1:8000/_account_settings_password_and_security.html
# http://127.0.0.1:8000/_account_settings_stats.html

# http://127.0.0.1:8000/_index_featured_jobs.html
# http://127.0.0.1:8000/_index_highest_rated_employees.html

# http://127.0.0.1:8000/_footer.html
# http://127.0.0.1:8000/_footer2a.html
# http://127.0.0.1:8000/_footer2b.html
# http://127.0.0.1:8000/_header.html
# http://127.0.0.1:8000/_headline.html
# http://127.0.0.1:8000/_headline2.html
# http://127.0.0.1:8000/_login.html
# http://127.0.0.1:8000/_logout.html
# http://127.0.0.1:8000/_popup_apply_for_a_job.html
# http://127.0.0.1:8000/_popup_make_an_offer.html
# http://127.0.0.1:8000/_popup_subscribe.html
# http://127.0.0.1:8000/_script.html
# http://127.0.0.1:8000/_sidebar.html
# http://127.0.0.1:8000/_sidebar2.html
# http://127.0.0.1:8000/_signin_form.html
# http://127.0.0.1:8000/_signup_form.html