_author_ = 'rwolf'
_project_ = 'FlaskByExample'

MOCK_USERS = {'test@example.com': '123456'}


class MockDBHelper:

    def get_user(self, email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None