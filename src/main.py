import time
import os
from watchdog.observers import Observer
from watcher.test_report_handler import TestReportHandler

# Folder to monitor
WATCH_FOLDER = "test_reports"
os.makedirs(WATCH_FOLDER, exist_ok=True)

# Start folder monitoring
observer = Observer()
event_handler = TestReportHandler()
observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
observer.start()

print(f"👀 Watching folder: {WATCH_FOLDER} for new test reports...")

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()



# import os
# import json
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from crewai import Task, Crew, Agent
# from dotenv import load_dotenv
#
# # Load environment variables
# load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")
#
# # folder to monitor
# WATCH_FOLDER = "test_reports"
#
#
# class TestReportHandler(FileSystemEventHandler):
#     """Monitors the folder and analyzes new test reports."""
#
#     def on_created(self, event):
#         if event.is_directory:
#             return
#
#         file_path = event.src_path
#         if file_path.endswith(".json"):
#             print(f"New test report detected: {file_path}")
#             analyze_test_report(file_path)
#
#
# def analyze_test_report(file_path):
#     """Reads the test report and uses CrewAI to analyze failures."""
#     try:
#         with open(file_path, "r") as file:
#             report_content = file.read()
#
#         # Define the CrewAI agent
#         test_analyzer = Agent(
#             role="Test Report Analyzer",
#             goal="Automatically extract and classify test failures from the report.",
#             backstory="""
#                 You are an expert QA engineer. You automatically analyze test reports,
#                 extract failing tests, and classify errors into meaningful categories (e.g., timeouts, assertions, etc.).
#             """,
#         )
#
#         # Define Task: Pass the entire content of the report to CrewAI for analysis
#         task = Task(
#             description=f"Analyze the following test report:\n\n{report_content}",
#             expected_output="Extract failing tests, classify errors and create a bug for me for each failed test. Give me a file with the bugs",
#             agent=test_analyzer,
#         )
#
#         # Initialize Crew
#         crew = Crew(agents=[test_analyzer], tasks=[task], verbose=True)
#
#         # Kickoff the analysis with CrewAI
#         results = crew.kickoff()
#
#         print("################### CrewAI Analysis Results #################")
#         print(results)
#
#     except Exception as e:
#         print(f"Error processing the test report: {e}")
#
#
# # Start watching the folder
# observer = Observer()
# event_handler = TestReportHandler()
# observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
# observer.start()
#
# print(f"Watching folder: {WATCH_FOLDER} for new test reports...")
#
# try:
#     while True:
#         time.sleep(5)
# except KeyboardInterrupt:
#     observer.stop()
#
# observer.join()
