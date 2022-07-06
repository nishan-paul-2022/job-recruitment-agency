from django.db import models


class Models_nationality(models.Model):
    nationality = models.TextField()


class Models_job_category(models.Model):
    job_category = models.TextField()


class Models_company_category(models.Model):
    company_category = models.TextField()


class Models_freelancer(models.Model):
    username = models.TextField()
    emailaddress = models.TextField()
    password = models.TextField()
    freelancer_picture = models.TextField()
    freelancer_name_first = models.TextField()
    freelancer_name_last = models.TextField()
    freelancer_type = models.TextField()
    freelancer_phone = models.TextField()
    freelancer_salary = models.TextField()
    freelancer_skills = models.TextField()
    freelancer_tagline = models.TextField()
    freelancer_nationality = models.TextField()
    freelancer_description = models.TextField()
    freelancer_stats_company = models.TextField()
    freelancer_stats_job = models.TextField()
    freelancer_stats_job_offers = models.TextField()
    freelancer_stats_job_proposals = models.TextField()


class Models_company(models.Model):
    company_username = models.TextField()
    username = models.TextField()
    company_picture = models.TextField()
    company_name = models.TextField()
    company_category = models.TextField()
    company_location = models.TextField()
    company_tagline = models.TextField()
    company_description = models.TextField()


class Models_job(models.Model):
    job_username = models.TextField()
    username = models.TextField()
    company_username = models.TextField()
    job_picture = models.TextField()
    job_timebegin = models.TextField()
    job_timeend = models.TextField()
    job_title = models.TextField()
    job_location = models.TextField()
    job_type = models.TextField()
    job_category = models.TextField()
    job_salary = models.TextField()
    job_postion = models.TextField()
    job_description = models.TextField()


class Models_job_proposals(models.Model):
    username = models.TextField()
    job_username = models.TextField()
    job_proposals_cv = models.TextField()


class Models_job_offers(models.Model):
    username = models.TextField()
    job_username = models.TextField()
    job_offers_email = models.TextField()
