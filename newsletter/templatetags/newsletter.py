"""
The newsletter template tag library

`{% load newsletter %}`

To use the newsletter template tags.  It is required
to have jquery.forms.js installed.

This is included with the installation under the `static` directory.

"""

from django import template
from django.core.urlresolvers import reverse

register = template.Library()

class NewsletterNode(template.Node):

    def render(self, context):
        return (
"""
<div id="newsletter_container" class="newsletter"></div>

<script type="text/javascript">
    $(document).ready(function() {
        $.get('%s', function(data) {
            $('#newsletter_container').html(data);
            $('#newsletter_signup_form').ajaxForm({
                'target': $('#newsletter_container'),
                'replaceTarget':true
            });
        });
    });
</script>
""" % reverse('newsletter:signup_form'))

@register.tag
def newsletter(parser, token):
    """
    The newsletter template tag will insert the necessary DOM elements to use
    the newsletter app correctly.

    To use:
        {% newsletter %}

    will create a `div` element with an id attribute `newsletter_container`

    This is where the ajax responses will place the returned HTML from the view.

    """
    return NewsletterNode()
