{% extends "base.tpl" %}
{% block content %}
<img src="screenshots/{{ title }}.png" class="center" alt="new_{{ title }}">
<br>
<h1 class="f-6 lh-solid gray bold center">{{ title }}</h1>
<h3 class="f-4 ml7 ph7 bold silver center f-subheadline lh-title">{{ description }}</h3><br><br>
<a href="{{ link }}" class="f1 lh-title washed-red fw6 ml5 ph7 db black link hover-dark-red">LINK</a>
{% endblock %}
