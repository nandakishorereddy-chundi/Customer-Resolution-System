from admin import Admin
from agent import Agent
from user import User
from transaction import Transaction
from issue_service import IssueService
from admin_service import AdminService
from customer_resolution_system import CustomerResolutionSystem


class Main:

    def create_admin(self):
        admin = Admin()
        admin.set_id('id1')
        admin.set_name('PhonePe')
        admin.set_email('admin@phonepe.com')
        return admin

    def create_users(self):
        users = []
        for i in range(1, 4):
            user = User()
            user.set_id('userId' + str(i))
            user.set_name('username' + str(i))
            user.set_email('username'+str(i)+'@gmail.com')
            users.append(user)
        return users

    def create_transactions(self):
        transactions = []
        for i in range(1, 3):
            transaction = Transaction()
            transaction.set_id('T' + str(i))
            transaction.set_user_id('user' + str(i))
            transaction.set_status('FAILED')
            transactions.append(transaction)
        return transactions

    def test(self):
        system = CustomerResolutionSystem()
        admin = self.create_admin()
        AdminService().add_agent('agentId1', 'Agent1', 'agent1@gmail.com', ['PAYMENT', 'GOLD'])
        users = self.create_users()
        transactions = self.create_transactions()
        issue = system.create_issue('T1', 'PAYMENT', 'payment failed', 'failed during transaction', 'username1@gmail.com')
        AdminService().view_agents_work_history()
        system.assign_issue(issue)
        AdminService().view_agents_work_history()
        system.get_issue({'email': 'username1@gmail.com'})
        system.update_issue(issue.get_id(), 'IN_PROGRESS', 'waiting for payment')
        system.resolve_issue(issue.get_id(), 'debited amount will be refunded')

main = Main()
main.test()