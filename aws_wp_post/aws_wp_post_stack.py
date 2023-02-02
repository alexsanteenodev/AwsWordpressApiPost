from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    aws_iam as _iam,
    aws_lambda_python_alpha as python,
    aws_events,
    aws_events_targets,
    Duration,
    aws_logs
)
from constructs import Construct
import os


class AwsWpPostStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # Create role for your Lambda function
        lambda_role = _iam.Role(scope=self, id='cdk-lambda-role',
                                assumed_by=_iam.ServicePrincipal(
                                    'lambda.amazonaws.com'),
                                role_name='cdk-lambda-role',
                                managed_policies=[
                                    _iam.ManagedPolicy.from_aws_managed_policy_name(
                                        'service-role/AWSLambdaVPCAccessExecutionRole'),
                                    _iam.ManagedPolicy.from_aws_managed_policy_name(
                                        'service-role/AWSLambdaBasicExecutionRole')
                                ]
                                )

        # create lambda stacks
        handler = python.PythonFunction(self, "WpPostHandler",
                                        runtime=lambda_.Runtime.PYTHON_3_9,
                                        entry='resources',
                                        index='wpPostHandler.py',
                                        handler="lambda_handler",
                                        role=lambda_role,
                                        # sets the timeout to 30 seconds
                                        timeout=Duration.seconds(30),
                                        log_retention=aws_logs.RetentionDays.THREE_DAYS,
                                        environment={
                                            "ENDPOINT_URL": os.environ['ENDPOINT_URL'],
                                            "AUTH_USERNAME": os.environ['AUTH_USERNAME'],
                                            "AUTH_PASSWORD": os.environ['AUTH_PASSWORD'],
                                            "OPENAI_API_KEY": os.environ['OPENAI_API_KEY'],
                                            "PUBLISHER_ENABLED": 'False',
                                        }
                                        )
        # event rule for invoking lambda function by schedule
        event_rule = aws_events.Rule(self, "scheduleRule",
                                     schedule=aws_events.Schedule.cron(
                                         minute='*/3'),
                                     )

        # add target to event rule
        event_rule.add_target(aws_events_targets.LambdaFunction(handler))
