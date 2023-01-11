from admin import Admin
from agent import Agent

class AdminService:
    admins = {}
    agents = {}
     
    def create_admin(self, id, name, email):
        admin = Admin()
        admin.set_id(id)
        admin.set_name(name)
        admin.set_email(email)
        self.__class__.admins[id] = admin
        return admin

    def add_agent(self, id, name, email, specializations):
        agent = Agent()
        agent.set_id(id)
        agent.set_name(name)
        agent.set_email(email)
        agent.set_specializations(specializations)
        self.__class__.agents[id] = agent
        print(f'agent {id} is created')
        return agent

    def view_agents_work_history(self):
        for agent in self.__class__.agents.values():
            print(f'id: {agent.get_id()}: [{agent.get_issues()}]')
