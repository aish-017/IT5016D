class Ticket:
    def __init__(self, staffID, name, email, description):
        # Initialize the ticket with staff details and issue description
        self.staffID = staffID
        self.name = name
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def __str__(self):
        # Format the ticket details for printing
        return (f"Ticket Number: {self.ticketNumber}\n"
                f"Ticket Creator: {self.name}\n"
                f"Staff ID: {self.staffID}\n"
                f"Email Address: {self.email}\n"
                f"Description: {self.description}\n"
                f"Response: {self.response}\n"
                f"Ticket Status: {self.status}")

class HelpDesk:
    # Static variables to keep track of ticket numbers and counts
    ticketNumber = 2000
    openTickets = 0
    closedTickets = 0

    def __init__(self):
        # Initialize the HelpDesk with an empty list of tickets
        self.tickets = []

    def submitTicket(self, staffID, name, email, description):
        # Create a new ticket with staff details and issue description
        newTicket = Ticket(staffID, name, email, description)
        self.tickets.append(newTicket)
        newTicket.ticketNumber = HelpDesk.ticketNumber
        HelpDesk.ticketNumber += 1
        HelpDesk.openTickets += 1
        # Check if the ticket is for a password change
        if "Password Change" in description:
            newTicket.response = f"New password generated: {staffID[:2]}{name[:3]}"
            HelpDesk.closedTickets += 1
            HelpDesk.openTickets -= 1
            newTicket.status = "Closed"
        return newTicket

    def respondToTicket(self, ticketNumber, response):
        # Respond to an existing ticket by ticket number
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.response = response
                HelpDesk.closedTickets += 1
                HelpDesk.openTickets -= 1
                ticket.status = "Closed"

    def reopenTicket(self, ticketNumber):
        # Reopen a closed ticket by ticket number
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                ticket.status = "Reopened"
                HelpDesk.openTickets += 1
                HelpDesk.closedTickets -= 1

    def displayTicket(self, ticketNumber):
        # Display the details of a specific ticket by ticket number
        for ticket in self.tickets:
            if ticket.ticketNumber == ticketNumber:
                print(ticket)

    def displayStatistics(self):
        # Display the overall statistics of the HelpDesk
        print(f"Tickets Created: {HelpDesk.ticketNumber - 2000}")
        print(f"Tickets Resolved: {HelpDesk.closedTickets}")
        print(f"Tickets To Solve: {HelpDesk.openTickets}")

    def displayAllTickets(self):
        # Display the details of all tickets
        for ticket in self.tickets:
            print(ticket)
            print()

def main():
    # Create a HelpDesk object to manage tickets
    helpDesk = HelpDesk()
    
    # Submit tickets with details for Inna, Maria, and John
    helpDesk.submitTicket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    helpDesk.submitTicket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Requested for a videocamera to conduct webinars")
    helpDesk.submitTicket("JOHNS", "John", "john@whitecliffe.co.nz", " Requires password change")

    # Display the current statistics and all tickets
    helpDesk.displayStatistics()
    helpDesk.displayAllTickets()

    # Respond to Inna's ticket and update the status
    helpDesk.respondToTicket(2001, "The monitor has been replaced.")
    
    # Display the updated statistics and all tickets
    helpDesk.displayStatistics()
    helpDesk.displayAllTickets()

# Call the main function to run the HelpDesk system
if __name__ == "__main__":
    main()
