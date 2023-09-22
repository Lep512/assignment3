class Ticket:
    idcounter = 1
    def __init__(self):
        self.id = None
        self.staff_id = None
        self.creator = None
        self.contact_email = None
        self.description = ''
        self.response = 'Not Yet Provided'
        self.status = None
    
    def create_ticket(self, staffID, creator, contactEmail, description = None):
        self.id = Ticket.idcounter + 2000
        Ticket.idcounter += 1 
        self.staff_id = staffID
        self.creator = creator
        self.contact_email = contactEmail
        self.status = 'Open'
        if description:
            self.description = description
        self.password_change()
    
    def password_change(self):
        if "password change" in self.description.lower():
            self.generate_password()
        
    def generate_password(self):
        password = self.staff_id[:2] + self.creator[:3]
        self.response = 'New password generated: ' + password
        self.status = 'Closed'
    
    def response_ticket(self, response):
        self.response = response
        self.status = 'Closed'
    
        
    def reopen_ticket(self):
        self.status = 'Reopened'
    
    def resolve_ticket(self):
        self.status = 'Closed'
    
    def TicketStats(self):
        print('\nTicket Number: {}'.format(self.id))
        print('Ticket Creator: {}'.format(self.creator))
        print('Staff ID: {}'.format(self.staff_id))
        print('Email Address: {}'.format(self.contact_email))
        print('Description: {}'.format(self.description))
        print('Response: {}'.format(self.response))
        print('Ticket Status: {}\n'.format(self.status))

class Main():
    def __init__(self):
        self.tickets = []
    
    def get_ticket_info(self):
        print('You need to provide the following information to create a ticket.')
        staff_id = input("What is your staff ID, please: ")
        creator = input("what is your name, please: ")
        email = input("what is your email, please: ")
        description = input("Provide the description of your issue, please: ")
        return staff_id, creator, email, description
    
    def statistic(self):
        ticket_resolved = []
        ticket_to_solve = []
        for t in self.tickets:
            if t.status == 'Reopened' or t.status == 'Open':
                ticket_to_solve.append(t)
            if t.status == 'Closed':
                ticket_resolved.append(t)
        
        print('\nTickets Created: {}'.format(len(self.tickets)))
        print('Tickets Resolved: {}'.format(len(ticket_resolved)))
        print('Tickets To Solve: {}\n'.format(len(ticket_to_solve)))

    
    def print_tickets_info(self):
        for t in self.tickets:
            t.TicketStats()

    def main(self):
        print('Welcome to Help Desk Ticketing System.\n')
        ticket1 = Ticket()
        ticket2 = Ticket()
        ticket3 = Ticket()
        
        staff_id, creator,email, description = self.get_ticket_info()
        ticket1.create_ticket(staff_id, creator, email, description)
        self.tickets.append(ticket1)
        self.statistic()

        ## try to input 'password change' in the description in this ticket
        staff_id, creator,email, description = self.get_ticket_info()
        ticket2.create_ticket(staff_id, creator, email, description)
        self.tickets.append(ticket2)
        self.statistic()

        staff_id, creator,email, description = self.get_ticket_info()
        ticket3.create_ticket(staff_id, creator, email, description)
        self.tickets.append(ticket3)
        self.statistic()

        print('IT technicain response to resolve ticket3.')
        ticket3.response_ticket('The monitor has been replaced.')
        self.statistic()

        #resolve ticket1
        print('IT technicain tries to resolve ticket1.')
        ticket1.resolve_ticket()
        self.statistic()

        ## reopen ticket1
        print('IT technicain tries to reopen ticket1.')
        ticket1.reopen_ticket()
        self.statistic()

        print('The following are the information of all tickets.')
        self.print_tickets_info()


if __name__ == '__main__':
    m = Main()
    m.main()   

    