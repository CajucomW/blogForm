# Blog Form

A simple, Django-powered form I learned about from <a target="_blank" href="http://www.kickstartcoding.com">KickStart Coding</a> bootcamp. It's a feature that I'd love to, eventually, flesh out and add to my site.

The purpose of the app was to practice using django forms and models. I was going to leave styling out but couldn't (go figure). Playing around w/ bootstrap, but am having trouble styling the django form containing <code>csrf_token</code>.

To run the app:

- clone the repo
- in terminal run
    <code>pipenv shell</code>
    <code>python3 manage.py runserver</code>
- once finished, open up browser to localhost:8000

<h3>TODO:</h3>
<h4>06/09/20</h4>
<ul>
    <li>complete styling of <code>csrf_token</code></li>
    <li>views.py is a mess. consider using classes instead of functions</li>