import os
import json
from crewai import Task, Crew, Agent
from src.utils.bug_reporter import save_bug_report_tool

def analyze_test_report(file_path):
    """Reads a test report and extracts failing tests using CrewAI."""
    try:
        with open(file_path, "r") as file:
            report_content = file.read()

        # define my agent and pass the tool analyzer
        test_analyzer = Agent(
            role="Test Report Analyzer",
            goal="Extract failing tests and classify errors from test reports, show me the classified errors.",
            backstory="A QA expert who detects failed tests and categorizes them.",
            tools=[save_bug_report_tool],
        )

        # Define the task for the agent
        task = Task(
            description=f"Analyze the following test report:\n\n{report_content}",
            expected_output="Extract failing tests, classify errors, and save each bug report as a file.",
            agent=test_analyzer,
        )

        # Create Crew
        crew = Crew(agents=[test_analyzer], tasks=[task], verbose=True)

        # Start analysis
        results = crew.kickoff()
        print("🚀 CrewAI Analysis Completed!")
        print(results)

    except Exception as e:
        print(f"❌ Error processing test report: {e}")
