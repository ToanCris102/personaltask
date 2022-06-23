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
    api/auth/logout/                                blacklist refresh token
    api/auth/refresh-token/                         refresh token -> access token
    api/auth/profile/                               retrieve full profile and update full_name, email
    api/auth/profile/mode/                          update mode of profile
    api/auth/forgot-password-send-mail/             send token to user' mail
    api/auth/profile/change-password/               
    api/auth/change-password-with-token/            frontend puts the  access token in the mail pass in the header after pushing the new password

    api/workspaces/
    api/workspaces/<int:workspaces_id>/

    api/workspaces/<int:workspaces_id>/task/
    api/workspaces/<int:workspaces_id>/task/<int:task_id>/
}