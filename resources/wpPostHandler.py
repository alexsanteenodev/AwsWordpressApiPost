import os
import src.publisher.generate_publish_post as generate_publish_post
import calendar
import logging
import dateutil.parser

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Logs the call with a friendly message and the full event data.
    :param event: The event dict that contains the parameters sent when the function
                  is invoked.
    :param context: The context in which the function is called.
    :return: The result of the specified action.
    """
    if 'time' in event:
        dt = dateutil.parser.parse(event['time'])
        logger.info(
            "Lambda invoked on %s at %s.",
            calendar.day_name[dt.weekday()], dt.time().isoformat())
    logger.info("Full event: %s", event)

    print("os.environ", os.environ)
    # Generate a random post title
    if (os.getenv("PUBLISHER_ENABLED") is not None and os.environ["PUBLISHER_ENABLED"] == "True"):
        print("Publisher is enabled")
        generate_publish_post()
    else:
        print("Publisher is disabled")

    print("Handler finished")
