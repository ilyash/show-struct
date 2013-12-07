show-struct
===========

Shows possible jq paths in a JSON file


Sample usage (when in path):

    show_struct.py BLAH_CloudTrail_us-east-1_BLAH_sViXVfCImmbyVBO6.json

Sample usage (when not in path):

    ./show_struct.py BLAH_CloudTrail_us-east-1_BLAH_sViXVfCImmbyVBO6.json

Sample output:

    .Records -- (Array of 3 elements)
    .Records[]
    .Records[].awsRegion -- us-east-1
    .Records[].eventName -- DescribeInstances
    .Records[].eventSource -- ec2.amazonaws.com
    .Records[].eventTime -- 2013-12-06T10:34:34Z .. 2013-12-06T10:36:36Z (3 unique values)
    ...
    .Records[].sourceIPAddress -- 1.2.3.4 .. 5.6.7.8 (3 unique values)
