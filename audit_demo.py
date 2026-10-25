import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger("enterprise_ai")


def audit_event(
    user_id: str,
    action: str,
    outcome: str,
) -> None:
    logger.info(
        "user_id=%s action=%s outcome=%s",
        user_id,
        action,
        outcome,
    )


if __name__ == "__main__":
    audit_event(
        user_id="demo-user-123",
        action="search_documents",
        outcome="success",
    )