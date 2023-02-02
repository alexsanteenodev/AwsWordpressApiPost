#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_wp_post.aws_wp_post_stack import AwsWpPostStack


app = cdk.App()
AwsWpPostStack(app, "AwsWpPostStack")

app.synth()
