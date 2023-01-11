from issue import Issue, IssueType

class IssueService:
    issues = {}

    def create_issue(self, id, transaction_id, user_email, issue_type):
        issue = Issue()
        issue.set_id(id)
        issue.set_transaction_id(transaction_id)
        issue.set_user_email(user_email)
        issue.set_issue_type(issue_type)
        self.__class__.issues[id] = issue
        print(f'Issue {id} is created against transaction {transaction_id}')
        return issue

    def search_by_email(self, email):
        issue_list = []
        for id in self.__class__.issues:
            user_email = self.__class__.issues[id].get_user_email()
            if user_email == email:
                issue_list.append(self.__class__.issues[id])
        return issue_list

    def search_by_type(self, type):
        issue_list = []
        for id in self.__class__.issues:
            issue_type = self.__class__.issues[id].get_issue_type()
            if issue_type == type:
                issue_list.append(self.__class__.issues[id])
        return issue_list

    def search_by_id(self, id):
        return [issues[id]]

    def search_options(self, key):
        return {
            'email': self.search_by_email,
            'type': self.search_by_type,
            'id': self.search_by_id
        }.get(key, None)

    def get_issue(self, options):
        search_key = list(options.keys())[0]
        value = options[search_key]
        search = self.search_options(search_key)
        if not search:
            return []
        return search(value)