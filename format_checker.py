from jsonschema import validate
from jsonschema.exceptions import ValidationError

input_test_schema = {
    "type": "object",
    "properties": {
        "tag": {
            "type": "string"
        },
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    }
                },
                "required": [
                    "type",
                    "description"
                ]
            }
        }
    },
    "required": [
        "tag",
        "steps"
    ]
}

openai_output_schema = {
    "type": "object",
    "properties": {
        "label ID": {
            "type": "array"
        },
        "action": {
            "type": "string"
        }
    },
    "required": [
        "label ID",
        "action"
    ]
}

def validate_test_input(input: object):
    try:
        validate(input, input_test_schema)
        return True
    except ValidationError:
        return False


def validate_openai_output(input: object):
    try:
        validate(input, openai_output_schema)
        return True
    except ValidationError:
        return False