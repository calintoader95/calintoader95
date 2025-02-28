import os
from crewai.tools import BaseTool

# Directory to store generated bug reports
BUG_REPORTS_DIR = "bug_reports"
os.makedirs(BUG_REPORTS_DIR, exist_ok=True)

# my custom tool
class SaveBugReportTool(BaseTool):
    def __init__(self):
        super().__init__(name="Save Bug Report", description="Saves a bug report with details including test case, error message, category, and priority.")

    def _run(self, test_case: str, error_message: str, error_category: str, priority: str):
        """Creates a text file for each bug with details."""
        file_name = f"{test_case}_{priority}.txt".replace(" ", "_")
        file_path = os.path.join(BUG_REPORTS_DIR, file_name)

        with open(file_path, "w") as file:
            file.write(f"Bug Report\n==========\n")
            file.write(f"Test Case: {test_case}\n")
            file.write(f"Error Message: {error_message}\n")
            file.write(f"Error Category: {error_category}\n")
            file.write(f"Priority: {priority}\n")

        print(f"✅ Bug report saved: {file_path}")
        return f"Bug report saved at: {file_path}"

# Instantiate the tool
save_bug_report_tool = SaveBugReportTool()
