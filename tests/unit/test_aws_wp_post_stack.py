import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_wp_post.aws_wp_post_stack import AwsWpPostStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_wp_post/aws_wp_post_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsWpPostStack(app, "aws-wp-post")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
