import re
from .banner import BANNER
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
    def __init__(self, name, type, body_content):
        self.name = name
        self.type = type
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
        return list(self.template_engine.keys()) # simply listing out all our keys NOT values



class EmailTemplateEngine():
    """
    Email template
    Must contain {{subject}} and {{bodyContent}} placeholders

    Final output formatted as:
    Subject: <subject value>
    <bodyContent value>
    """
    # considering that this needs to handle its own rendering. And output it by itself. The Renderer only needs to call it, and this needs to be fully functional
    def formatted_output(self, template_engine, variables):
        pattern_finder = re.compile(r"{{(.*?)}}") # simple regex: find all things inside non greedy style, and list them as regex objects
        placeholders = pattern_finder.findall(template_engine.body_content)
        email_required_variables = ["subject", "bodyContent"]
        missing_variables = []

        for var in email_required_variables:
            if var not in variables:
                missing_variables.append(var)
        if missing_variables:
            raise Exception(f"Error: Missing variables: {','.join(missing_variables)}")


        required_placeholders_in_body = ["bodyContent"]
        missing_placeholders = [name for name in required_placeholders_in_body if name not in placeholders]
        if missing_placeholders:
            raise Exception(f"Error: Missing placeholders: {','.join(missing_placeholders)}")

        body = template_engine.body_content
        for p in placeholders:
            if p not in variables:
                raise Exception(f"Error: Missing placeholder: {p}")
            body = body.replace("{{" + p +"}}", variables[p])

        structured_output = f"Subject: {variables['subject']}\n \n{body}"
        return structured_output



class SocialMediaTemplateEngine():
    """
    Social media template
    Must Contain {{people_tagged}} & {{caption}} placeholders

    Final Output formatted as:
    Friends Taggged:{{people_tagged}}
    BANNER <- using ASCII inside of terminal (same generic image for each, no point in going over the top)
    Caption: {{caption}}
    """

    def formatted_output(self, template_engine, variables):
        pattern_finder = re.compile(r"{{(.*?)}}")  # simple regex: find all things inside non greedy style, and list them as regex objects
        placeholders = pattern_finder.findall(template_engine.body_content)
        email_required_variables = ["user", "caption"]
        missing_variables = []

        for var in email_required_variables:
            if var not in variables:
                missing_variables.append(var)
        if missing_variables:
            raise Exception(f"Error: Missing variables: {','.join(missing_variables)}")

        body = template_engine.body_content
        for p in placeholders:
            if p not in variables:
                raise Exception(f"Error: Missing placeholder: {p}")
            body = body.replace("{{" + p + "}}", variables[p])

        structured_output = f"{BANNER}\n{body}"
        return structured_output

    # same general logic as email template, only final output differently

class RenderTemplateEngine():
    """
    - take a template + dictionary/map of variables
    - replace placeholders (e.g., {{topic}}) with provided values
    - return the final rendered string
    - If a placeholder has no matching value, return a clear error or validation result.
    """
    def __init__(self):
        self.engine_type= {
            "email": EmailTemplateEngine(),
            "socialmedia": SocialMediaTemplateEngine(),
        }
    def render(self, template_name, handler, variables):
        template = handler.get_template_by_name(template_name)
        if template.type not in self.engine_type:
            raise Exception(
                f"Unknown template type: {template.type} -- Please use one of following {', '.join(self.engine_type.keys())}")
        engine = self.engine_type[template.type]
        output = engine.formatted_output(template, variables)
        return output

    # First match each of the templates
    # using regex (re) replace all the placeholders
    # Return String if no errors