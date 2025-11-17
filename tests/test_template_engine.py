from Prompt_template_managment.templates.template_engine import *

email_template = TemplateEngine("FarewellEmail", "email", "My name is {{userName}} and I want to thank you for coming to my {{bodyContent}}")
email_template_2 = TemplateEngine("Email", "Ali", "TEST_2")
handler = TemplateHandler()
handler.register_template(email_template)
rendering = RenderTemplateEngine()


output = (rendering.render(
    template_name ="FarewellEmail",
    variables = {
        "subject": "Thank you for having me!",
        "userName": "Ali",
        "bodyContent": "Demonstration!",
    },
    handler= handler,

))
print(output)
print(handler.list_templates())






