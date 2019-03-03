# Introduction

Team "uhh... foo bar?" at HooHacks 2019

# Docker

- To run container, run `docker-compose up`
- To stop the container in the current process `ctrl + c`
  - DOES NOT SHUT IT DOWN
- To stop container `docker-compose down`
  - Do this when you are done developing for the day / session

# If you are working on this in the future

- If you update the models, and want to use the different endpoints in [api_views](./hoohacks/equitunity/api_views.py), then make sure you update the serializers in [serializers.py](./hoohacks/equitunity/serializers.py).
- If you create a new page
  - You must add the url to [urls.py](./hoohacks/equitunity/urls.py)
    - You can pass in values like this `url(r'user_profile/(?P<pk>[0-9]+)', views.user_profile, name='user_profile')` where `?P<pk>` is the variable `pk` and the `[0-9]+` is a regex to match the pattern
  - Create a new view in [views.py](./hoohacks/equitunity/views.py)
    - You can create a:
      - `TemplateView`
      - `GenericView`
      - or as we did a method that returns a request

_Created By Anna Cuddeback, Chad Baily, and Will Scheib for HooHacks 2019_
