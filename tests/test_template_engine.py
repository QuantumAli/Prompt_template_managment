from Prompt_template_managment.templates.template_engine import *

# doing all of the tests
def test_email_template(handler, rendering):
    print("=== EMAIL TEMPLATE TEST ===")
    print("EXPECTED RESULT: PASS")
    email_template = TemplateEngine(
        "FarewellEmail",
        "email",
        "My name is {{userName}} and I want to thank you for coming to my {{bodyContent}}"
    )
    handler.register_template(email_template)

    output = rendering.render(
        template_name="FarewellEmail",
        variables={
            "subject": "Thank you for having me!",
            "userName": "Ali",
            "bodyContent": "Demonstration!",
        },
        handler=handler,
    )
    print(output, "\n")


def test_same_template_registered(handler):
    print("\n=== Same Template being registered")
    print("EXPECTED RESULT: ERROR")
    email_template_2 = TemplateEngine("FarewellEmail", "email", "TEST_2")  # same name
    handler.register_template(email_template_2)


def test_unregistered_template(rendering, handler):
    print("\n=== UNREGISTERED TEST ===")
    print("EXPECTED RESULT: ERROR")
    output = rendering.render(
        template_name="DoesNotExist",  # name not registered
        handler=handler,
        variables={
            "subject": "Thank you for having me!",
            "userName": "Ali",
            "bodyContent": "Demonstration!",
        }
    )


def test_social_media_success(handler, rendering):
    print("\n=== Social media template being registered ===")
    print("EXPECTED RESULT: PASS")
    social_template = TemplateEngine(
        "post",
        "socialmedia",
        "Friends tagged: {{user}}\n\nCAPTION:\n{{caption}}\n"
    )
    handler.register_template(social_template)
    output = rendering.render(
        "post",
        handler=handler,
        variables={
            "user": "@QuantumAli",
            "caption": "Just shipped my prompt template engine! 🚀"
        }
    )
    print(output)


def test_social_media_missing_vars(handler, rendering):
    print("\n=== MISSING REQUIRED VARIABLES (SOCIAL MEDIA)===")
    print("EXPECTED RESULT: ERROR")

    # make sure the template exists for this test
    social_template = TemplateEngine(
        "post_missing_vars",
        "socialmedia",
        "Friends tagged: {{user}}\n\nCAPTION:\n{{caption}}\n"
    )
    handler.register_template(social_template)

    # now call render with a missing 'user' on purpose
    output = rendering.render(
        "post_missing_vars",
        handler=handler,
        variables={
            # missing 'user' on purpose
            "caption": "Just shipped my prompt template engine! 🚀"
        }
    )

def test_email_missing_variables(handler, rendering):
    print("\n=== EMAIL TEMPLATE MISSING VARIABLES ===")
    print("EXPECTED RESULT: ERROR")
    email_template = TemplateEngine(
        "EmailMissingVars",
        "email",
        "Hi {{userName}}, thanks for coming to my {{bodyContent}}"
    )
    handler.register_template(email_template)

    # Missing 'bodyContent' on purpose
    output = rendering.render(
        template_name="EmailMissingVars",
        handler=handler,
        variables={
            "subject": "Thanks!",
            "userName": "Ali",
            # "bodyContent": "Demo"  # intentionally missing
        }
    )


def test_email_missing_placeholder_value(handler, rendering):
    print("\n=== EMAIL TEMPLATE EXTRA PLACEHOLDER WITH NO VALUE ===")
    print("EXPECTED RESULT: ERROR")
    email_template = TemplateEngine(
        "EmailExtraPlaceholder",
        "email",
        "Hi {{userName}}, this is {{bodyContent}} about {{extra}}"
    )
    handler.register_template(email_template)

    # 'extra' placeholder exists in body but not in variables
    output = rendering.render(
        template_name="EmailExtraPlaceholder",
        handler=handler,
        variables={
            "subject": "Extra test",
            "userName": "Ali",
            "bodyContent": "a demo",
            # "extra": "something"  # intentionally missing
        }
    )


def test_unknown_template_type(handler, rendering):
    print("\n=== UNKNOWN TEMPLATE TYPE ===")
    print("EXPECTED RESULT: ERROR")
    unknown_template = TemplateEngine(
        "unknownTemplate",
        "unknown",
        "Just an unknown template with {{userName}}"
    )
    handler.register_template(unknown_template)

    output = rendering.render(
        template_name="unknownTemplate",
        handler=handler,
        variables={
            "userName": "Ali"
        }
    )

def test_list_templates(handler):
    print("\n=== LISTING TEMPLATES ===")
    print(handler.list_templates())


if __name__ == "__main__":
    handler = TemplateHandler()
    rendering = RenderTemplateEngine()

    # test_email_template(handler, rendering)
    # test_same_template_registered(handler)
    # test_unregistered_template(rendering, handler)
    # test_social_media_success(handler, rendering)
    test_social_media_missing_vars(handler, rendering)
    # test_list_templates(handler)
    # test_email_missing_placeholder_value(handler, rendering)
    # test_unknown_template_type(handler, rendering)