from typing import Dict

class FillFormTool:
    def fill_form(self, form_type: str, user_data: Dict[str, str]) -> Dict[str, str]:
        mock_fields = {
            "GI Bill": ["name", "dob", "service_branch", "separation_date", "email"],
            "Tuition Assistance": ["name", "military_status", "unit", "email"],
        }
        required_fields = mock_fields.get(form_type, [])
        return {field: user_data.get(field, "N/A") for field in required_fields}

class SubmitFormTool:
    def submit_form(self, form_data: Dict[str, str]) -> str:
        return f"Form submitted with the following data:\n{form_data}\n\nNote: No sensitive data stored. Please confirm submission with the relevant authority."
