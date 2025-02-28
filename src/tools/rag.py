from crewai_tools.tools.rag.rag_tool import RagTool


def load_and_query_report(file_path):
    print(f"Loading file: {file_path}")
    rag_tool = RagTool().from_file(file_path)

    # Query the loaded knowledge base
    response = rag_tool.query("What are the common errors in the test checkout?")
    print(f"Query response: {response}")

    return response
