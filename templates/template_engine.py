import re
"""
KEY DISCLAIMER: I am writing a lot of comments to explain my thought process. 
Esp during testing/prelim phase I want to see exactly how I am doing this, and what I am trying to achieve
All unnecesary comments are removed before final git push (presuming system works) 
"""

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
    """
    add/register templates
    retrieve a template by name
    list all templates
    """
    def __init__(self):
        self.template_engine = {} #making it empty so that it can be filled with the template class, each individual template class. In essence, this is going to be our memory + our handler

    def register_template(self, template):
        if template.name in self.template_engine: # in works here because it checks keys not values
            print(f"{template.name} Template already registered")
            raise Exception('Error: Template already registered')
        self.template_engine[template.name] = template # for all other cases
        print(f"{template.name} Template registered")
        # two things: no need to return bc it is self, and secondly, we are storing the entire template contents per name
        # Such as "{{name}}, {{subject}} and {{content}} -> all inside of Email, or social media. Right now it is a dict.

    def get_template_by_name(self, name):
        if name in self.template_engine:
            return self.template_engine[name]
        print("Template not registered")
        raise Exception('Error: Template not registered')


    def list_templates(self):
        return self.template_engine.keys() # simply listing out all our keys NOT values



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