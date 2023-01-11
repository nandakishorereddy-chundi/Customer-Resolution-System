from ticket import Ticket

class TicketService:
    tickets = {}

    def create_ticket(self, id, issue_id, agent_id, status, description):
        ticket = Ticket()
        ticket.set_id(id)
        ticket.set_issue_id(issue_id)
        ticket.set_agent_id(agent_id)
        ticket.set_status(status)
        ticket.set_resolution(description)
        self.__class__.tickets[id] = ticket
        return ticket

    def get_ticket(self, issue_id):
        for ticket in self.__class__.tickets.values():
            if ticket.get_issue_id() == issue_id:
                return ticket
        return {}

    def update_issue(self, issue_id, status, resolution):
        ticket = self.get_ticket(issue_id)
        ticket.set_status(status)
        ticket.set_resolution(resolution)
        print(f'{issue_id} status updated to {status}')
        return ticket

    def resolve_issue(self, issue_id, resolution):
        ticket = self.get_ticket(issue_id)
        ticket.set_status('RESOLVED')
        ticket.set_resolution(resolution)
        print(f'{issue_id} marked resolved')
        return ticket