"""Google ADK Platform Runtime Entrypoint."""

import argparse
import sys

from arima_agent_platform.infrastructure.adk.agent_runner import ADKAgentRunner
from arima_agent_platform.infrastructure.config.settings import AppSettings
from arima_agent_platform.infrastructure.observability.logging import (
    StructuredLogger,
    configure_logging,
)

logger = StructuredLogger("arima_agent_platform.run")


def main() -> None:
    parser = argparse.ArgumentParser(description="ARIMA Agent Platform ADK Runtime")
    parser.add_argument(
        "--check", action="store_true", help="Verify Google ADK runtime initialization"
    )
    args = parser.parse_args()

    configure_logging()
    logger.info("Initializing Google ADK Agent Platform Runtime")

    settings = AppSettings()
    runner = ADKAgentRunner(settings=settings)
    adk_runner = runner.initialize_runtime()

    if args.check:
        print(f"Google ADK Runtime initialized successfully. App Name: {adk_runner.app_name}")
        sys.exit(0)

    print("ARIMA Agent Platform Google ADK Runtime active.")


if __name__ == "__main__":
    main()
