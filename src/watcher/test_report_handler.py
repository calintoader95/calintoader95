import os
from watchdog.events import FileSystemEventHandler
from src.ai_agents.test_agent import analyze_test_report

class TestReportHandler(FileSystemEventHandler):
    """Watches for new test reports and triggers analysis."""

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        if file_path.endswith(".json"):
            print(f"🆕 New test report detected: {file_path}")
            analyze_test_report(file_path)
