# Payment Agent
class PaymentAgent:

    def __init__(self):
        self.payments = {
            "1001": "Paid",
            "1002": "Pending",
            "1003": "Failed"
        }

    def check_payment(self, order_id):

        print("\n[Payment Agent Activated]")

        status = self.payments.get(order_id)

        if status is None:
            return "Payment record not found"

        elif status == "Paid":
            return "Payment already completed"

        elif status == "Pending":
            return "Payment is still pending"

        elif status == "Failed":
            return "Payment failed. Please retry"


# Support Agent
class SupportAgent:

    def handle_issue(self, issue):

        print("\n[Support Agent Activated]")
        print("Issue:", issue)

        if issue == "Payment Failed":
            print("Support checking payment gateway...")
            return "ESCALATE_ADMIN"

        else:
            print("Support resolved the issue.")
            return "RESOLVED"


# Admin Agent
class AdminAgent:

    def intervene(self, issue):

        print("\n[Admin Agent Activated]")
        print("Admin reviewing issue:", issue)

        if issue == "Payment Gateway Issue":
            print("Admin contacting payment provider...")
            print("Admin resolved payment gateway problem")

        else:
            print("Admin handled the issue")

        print("Issue closed by Admin\n")


# Main Program
def main():

    print("===================================")
    print("     Payment Management System")
    print("===================================")

    payment_agent = PaymentAgent()
    support_agent = SupportAgent()
    admin_agent = AdminAgent()

    print("\n--- Payment Section ---")

    order_id = input("Enter Order ID: ")

    result = payment_agent.check_payment(order_id)

    print(result)

    if result == "Payment failed. Please retry":

        support_response = support_agent.handle_issue("Payment Failed")

        if support_response == "ESCALATE_ADMIN":
            admin_agent.intervene("Payment Gateway Issue")


# Run Program
if __name__ == "__main__":
    main()
