---
layout: archive
title: "Publications"
permalink: /academic/publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% if site.publications.size > 0 %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% else %}
  <p>Coming soon! I am currently working on documenting my research and professional publications. Stay tuned for updates on my latest work in Data Engineering and AI.</p>
{% endif %}
