from knowledge import search_documents

APPLICATIONS = {
    "reporting": {
        "name": "Reporting Application",
        "owner": "Business Reporting Team",
        "support_route": "Submit an internal support request",
    },
    "timekeeping": {
        "name": "Timekeeping Application",
        "owner": "Human Resources Systems Team",
        "support_route": "Contact the internal HR systems support team",
    },
}


def search_company_documents(query: str) -> dict:
    """Search the sample company documentation."""

    results = search_documents(query)

    return {
        "results": [
            {
                "title": doc["title"],
                "content": doc["content"],
            }
            for doc in results
        ]
    }


def lookup_application(application_name: str) -> dict:
    """Look up a known application in the sample catalog."""

    query = application_name.lower()

    for key, application in APPLICATIONS.items():
        if key in query or query in application["name"].lower():
            return application

    return {"error": "Application not found"}