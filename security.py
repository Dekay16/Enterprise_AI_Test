DOCUMENTS = [
    {
        "id": "access-policy",
        "title": "Internal Application Access Policy",
        "allowed_groups": ["AllEmployees"],
        "content": (
            "Employees request application access through "
            "the approved access request process."
        ),
    },
    {
        "id": "hr-guide",
        "title": "HR Operations Guide",
        "allowed_groups": ["HR"],
        "content": (
            "HR staff use the internal HR operations guide "
            "for employee administration procedures."
        ),
    },
]


def search_authorized_documents(
    employee_groups: list[str],
    query: str,
) -> list[dict]:
    """Search only documents the employee is allowed to read."""

    allowed = []

    for document in DOCUMENTS:
        has_permission = any(
            group in employee_groups
            for group in document["allowed_groups"]
        )

        if has_permission:
            allowed.append(document)

    # Very basic word matching for this demonstration.
    words = set(query.lower().split())

    results = [
        document
        for document in allowed
        if words.intersection(
            set(document["title"].lower().split())
            | set(document["content"].lower().split())
        )
    ]

    return results