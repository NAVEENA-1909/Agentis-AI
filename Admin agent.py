# Customer Agent
class CustomerAgent:
    def handle_request(self, request):

        if "complaint" in request.lower() or "refund" in request.lower():
            return "ESCALATE_SUPPORT"

        elif "order status" in request.lower():
            return "CHECK_ORDER"

        else:
            return "Customer request handled by Customer Agent"


# Order Management Agent
class OrderAgent:
    def __init__(self):
        self.orders = {
            "1001": "Shipped",
            "1002": "Processing",
            "1003": "Delivered"
        }

    def check_order(self, order_id):

        status = self.orders.get(order_id)

        if status is None:
            return "ESCALATE_SUPPORT"

        else:
            return f"Order Status: {status}"


# Support Agent
class SupportAgent:
    def handle_issue(self, issue):

        print("\n[Support Agent Activated]")
        print("Issue Received:", issue)

        if issue == "Refund Request":
            print("Support checking refund policy...")
            return "ESCALATE_ADMIN"

        elif issue == "Customer Complaint":
            print("Support reviewing complaint...")
            return "ESCALATE_ADMIN"

        elif issue == "Order Not Found":
            print("Support verifying order details...")
            return "RESOLVED"

        else:
            print("Support resolved the issue.")
            return "RESOLVED"


# Admin Agent
class AdminAgent:

    def __init__(self):
        self.admin_actions = [
            "Refund Approved",
            "Complaint Escalated",
            "Order Issue Fixed"
        ]

    def intervene(self, issue):

        print("\n================================")
        print("       [Admin Agent Activated]")
        print("================================")

        print("Issue received from Support Agent:", issue)
        print("Admin reviewing the issue...")

        if issue == "Serious Customer Complaint":
            print("Admin investigating complaint...")
            print("Admin Action:", self.admin_actions[1])

        elif issue == "Refund Request":
            print("Admin verifying refund request...")
            print("Admin Action:", self.admin_actions[0])

        elif issue == "Order System Issue":
            print("Admin checking order database...")
            print("Admin Action:", self.admin_actions[2])

        else:
            print("Admin handled the issue successfully.")

        print("Admin has taken necessary action.")
        print("Issue closed by Admin Agent.\n")


# Main Program
def main():

    print("========================================")
    print("==== AI Customer Support Multi Agent ====")
    print("========================================")

    customer_agent = CustomerAgent()
    order_agent = OrderAgent()
    support_agent = SupportAgent()
    admin_agent = AdminAgent()

    # Customer Request Section
    print("\n--- Customer Request Section ---")

    request = input("Enter Customer Request: ")

    response = customer_agent.handle_request(request)

    if response == "ESCALATE_SUPPORT":

        support_response = support_agent.handle_issue("Customer Complaint")

        if support_response == "ESCALATE_ADMIN":
            admin_agent.intervene("Serious Customer Complaint")

    elif response == "CHECK_ORDER":

        order_id = input("Enter Order ID: ")
        order_status = order_agent.check_order(order_id)

        if order_status == "ESCALATE_SUPPORT":

            support_response = support_agent.handle_issue("Order Not Found")

            if support_response == "ESCALATE_ADMIN":
                admin_agent.intervene("Order System Issue")

        else:
            print(order_status)

    else:
        print("Customer Agent:", response)


# Run Program
if __name__ == "__main__":
    main()
