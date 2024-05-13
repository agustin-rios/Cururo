import json

class CodeReviewProcessor:
    def __init__(self, response_string):
        """
        Initialize with a JSON-formatted string response.
        """
        self.response = self.parse_response(response_string)

    @staticmethod
    def parse_response(response_string):
        """
        Parse the JSON string into a Python dictionary.
        """
        try:
            return json.loads(response_string)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON provided")

    def generate_commit_message(self):
        """
        Extract and format the commit message section.
        """
        message_info = self.response.get('message', {})
        return (f"Commit Message: {message_info.get('message', 'N/A')}\n"
                f"Adherence: {message_info.get('adherence', 'N/A')}\n"
                f"Completeness: {message_info.get('completeness', 'N/A')}")

    def generate_code_review(self):
        """
        Extract and format the code review details.
        """
        code_info = self.response.get('code', {})
        complexity = code_info.get('complexity_comment', 'N/A')
        acid_scores = code_info.get('acid_score', {})
        acid_comments = code_info.get('acid_comment', {})
        vulnerable = code_info.get('vulnerable_code', {})

        acid_report = "\n".join(
            f"{key.upper()} - Score: {acid_scores.get(key, 'N/A')}, Comment: {acid_comments.get(key, 'N/A')}"
            for key in ['a', 'c', 'i', 'd']
        )

        vulnerability_report = (f"Vulnerability Section: {vulnerable.get('section', 'N/A')}\n"
                                f"Vulnerability Comment: {vulnerable.get('comment', 'N/A')}\n"
                                f"Vulnerability Score: {vulnerable.get('score', 'N/A')}")

        return f"Complexity Comment: {complexity}\nACID Report:\n{acid_report}\nVulnerability Details:\n{vulnerability_report}"

    def create_full_report(self):
        """
        Combine all sections into a full report.
        """
        commit_message = self.generate_commit_message()
        code_review_details = self.generate_code_review()
        return f"{commit_message}\n\n{code_review_details}"


if __name__ == '__main__':
    # Usage
    response_string = '{"message": {"message": "Update function logic", "adherence": "5/5 😊", "completeness": "4/5 😊"}, "code": {"complexity_comment": "This change increases complexity significantly", "acid_score": {"a": "3/5 😐", "c": "4/5 😊", "i": "5/5 😊", "d": "2/5 😞"}, "acid_comment": {"a": "Good atomicity", "c": "Consistency could be improved", "i": "Excellent isolation", "d": "Durability needs attention"}, "vulnerable_code": {"section": "Line 45-50", "comment": "Potential SQL injection vulnerability", "score": "2/5 😞"}}}'
    processor = CodeReviewProcessor(response_string)
    full_report = processor.create_full_report()
    print(full_report)
