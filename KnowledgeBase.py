import tkinter as tk
from tkinter import messagebox

# Sample knowledge base data (replace this with your actual data)
knowledge_base = {
    'Phone Change, Add a phone etc.': 'Have them visit tech.rochester.edu and select Submit Service Request. An FAO number is needed to fill out the form. They will need to get that from their department. ',
    'Network Drop': ' Go to tech.rochester.edu, Submit Service Request -> Select Phone',
    'CTS MOC phone escalation ': 'Get the customers information. Issue(s) with the phone: Phone type (color, # of buttons):Phone number to be repaired:Who needs the phone repaired:Location of the phone to be repaired (Address/Suite/Room #):Number of individuals impacted:Did the customer request urgent service (yes or no):If the situation is affecting patient care immediately escalate to the CTS MOC with this information in a ticket assigned to TriageIf the situation can wait to be resolved, create a ticket and assign to Triage. Does this line need to be forwarded (yes or no):If yes, which number should it forward to:Contact name (First and last):Contact #: (Not the phone that needs repair.)Make a ticket and escalated to either the CTS MOC or Triage depending on the urgency of the issue. DO NOT transfer phone issues to ISD Helpdesk. ',
    # Add more issues and solutions as needed
}

class KnowledgeBaseViewer:
    def __init__(self, master):
        self.master = master
        self.master.title("Knowledge Base Viewer")

        self.issue_label = tk.Label(master, text="Select an Issue:")
        self.issue_label.pack(pady=10)

        self.issue_var = tk.StringVar()
        self.issue_var.set(list(knowledge_base.keys())[0])  # Default to the first issue
        self.issue_dropdown = tk.OptionMenu(master, self.issue_var, *knowledge_base.keys())
        self.issue_dropdown.pack(pady=10)

        self.view_button = tk.Button(master, text="View Solution", command=self.view_solution)
        self.view_button.pack(pady=10)

        self.solution_text = tk.Text(master, height=10, width=50, wrap=tk.WORD)
        self.solution_text.pack(pady=10)

    def view_solution(self):
        selected_issue = self.issue_var.get()
        solution = knowledge_base.get(selected_issue, "Solution not found.")
        self.solution_text.delete(1.0, tk.END)
        self.solution_text.insert(tk.END, solution)

if __name__ == "__main__":
    root = tk.Tk()
    app = KnowledgeBaseViewer(root)
    root.mainloop()
