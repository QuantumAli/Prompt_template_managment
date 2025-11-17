from Prompt_template_managment.templates.template_engine import *

email_template = TemplateEngine("Email", "Ali", "TEST")
email_template_2 = TemplateEngine("Email", "Ali", "TEST_2")
handler = TemplateHandler()
handler.register_template(email_template)
print(list(handler.list_templates()))
# PASS PRETEST FOR HANDLER