import datetime
from collections import deque

from admin_service import AdminService
from issue_service import IssueService
from ticket_service import TicketService

from issue import IssueType as issue_types

class CustomerResolutionSystem:
    def __init__(self):
        self.queues = {}
        for issue_type in issue_types:
            self.queues[issue_type.name] = deque()

    def get_free_agents(self):
        free_agents = []
        agents = AdminService.agents
        for agent in agents.values():
            if len(agent.get_issues()) == 0:
                free_agents.append(agent)
        return free_agents

    def assign_issue(self, issue):
        free_agents = self.get_free_agents()
        issue_assigned = False
        for agent in free_agents:
            if issue.get_issue_type() in agent.get_specializations():
                agent.add_issue(issue)
                print(f'Issue {issue.get_id()} is assigned to agent {agent.get_id()}')
                ticket = TicketService().create_ticket(issue.get_id(), issue.get_id(), agent.get_id(), 'OPEN', issue.get_description())
                issue_assigned = True
                break
        if not issue_assigned:
            self.queues[issue.get_issue_type()].append(issue)

    def get_issue(self, options):
        issue = IssueService().get_issue(options)[0]
        print(f'{issue.get_id()} {issue.get_transaction_id()} {issue.get_user_email()} {issue.get_issue_type()}')
        return issue

    def update_issue(self, issue_id, status, resolution):
        return TicketService().update_issue(issue_id, status, resolution)

    def resolve_issue(self, issue_id, resolution):
        return TicketService().resolve_issue(issue_id, resolution)

    def add_agent(self, email, name, specializations):
        id = len(AdminService().agents) + 1
        return AdminService().add_agent('agentID' + str(id), name, email, specializations)

    def create_issue(self, transaction_id, issue_type, subject, description, user_email):
        id = len(IssueService().issues) + 1
        return IssueService().create_issue('issueId' + str(id), transaction_id, user_email, issue_type)
