from security import search_authorized_documents


def test_employee_cannot_read_hr_document():
    results = search_authorized_documents(
        employee_groups=["AllEmployees"],
        query="HR Operations Guide",
    )

    assert all(
        document["id"] != "hr-guide"
        for document in results
    )


def test_hr_can_read_hr_document():
    results = search_authorized_documents(
        employee_groups=["HR"],
        query="HR Operations Guide",
    )

    assert any(
        document["id"] == "hr-guide"
        for document in results
    )