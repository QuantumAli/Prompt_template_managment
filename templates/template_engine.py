import re

# Simple way to create Template --> prototype to start, looking at optimizations later
# Focusing on a modular system, Strategy Pattern, marking off project req as I go

class TemplateEngine():
    """
    name (string, unique)
    type (string, e.g. "email", "summary", "chat")
    body (string with placeholders like {{userName}})
    """
    def __init__(self, name, _type, body_content):
        self.name = name
        self._type = _type
        self.body_content = body_content

class TemplateHandler():
    def __init__(self):
        self.template_engine = {} #making it empty so that it can be filled with the template class

    def register_template(self):
        return self # placeholder right now

    def get_template_by_name(self):
        return self

    def list_templates(self):
        return self

class EmailTemplateEngine():
    """
    Email template
    Must contain {{subject}} and {{bodyContent}} placeholders

    Final output formatted as:
    Subject: <subject value>
    <bodyContent value>

    """
    def __init__(self):
        self.template_engine = {}

    # rules and logic to handle how the template is treated
    # error check is located inside of here
    # return output

class SocialMediaTemplateEngine():
    """
    Social media template
    Must Contain {{people_tagged}} & {{caption}} placeholders

    Final Output formatted as:
    Friends Taggged:{{people_tagged}}
    BANNER <- using ASCII inside of terminal (same generic image for each, no point in going over the top)
    Caption: {{caption}}
    """
    def __init__(self):
        self.template_engine = {}

    # same general logic as email template, only final output differently

class RenderTemplateEngine():
    """
    - take a template + dictionary/map of variables
    - replace placeholders (e.g., {{topic}}) with provided values
    - return the final rendered string
    - If a placeholder has no matching value, return a clear error or validation result.
    """
    def __init__(self):
        self.template_engine = {}

    # First match each of the templates
    # using regex (re) replace all the placeholders
    # Return String if no errors