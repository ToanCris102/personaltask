enviroment: {
    Django==4.0.5
    django-filter==22.1
    djangorestframework==3.13.1
    djangorestframework-simplejwt==5.2.0
    Pillow==9.1.1
    psycopg2==2.9.3
    PyJWT==2.4.0
}

URL for API: {
    api/auth/register/
    api/auth/login/
    api/auth/logout/
    api/auth/refresh-token/
    api/auth/forgot-password/
    api/auth/change-password/
    api/auth/change-password-with-token/

    api/workspaces/
    api/workspaces/<int:workspaces_id>/

    api/workspaces/<int:workspaces_id>/task/
    api/workspaces/<int:workspaces_id>/task/<int:task_id>/
}