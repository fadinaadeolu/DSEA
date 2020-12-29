provider "aws" {
    region = "eu-central-1"
    access_key = var.access_key
    secret_key = var.secret_key
}

# Create server
resource "aws_transfer_server" "my_sftp_server" {
  identity_provider_type = "SERVICE_MANAGED" 
  tags = {
    NAME = "tf-acc-test-transfer-server"
    ENV  = "test"
  }
}

# Create IAM role
resource "aws_iam_role" "my_sftp_iam_role" {
  name = "tf-test-transfer-user-iam-role"
  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "transfer.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}
# Create IAM Policy
resource "aws_iam_role_policy" "my_sftp_iam_policy" {
  name = "tf-test-transfer-user-iam-policy"
  role = aws_iam_role.my_sftp_iam_role.id
  policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowFullAccesstoS3",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": "*"
        }
    ]
}
POLICY
}

# Create user
resource "aws_transfer_user" "my_sftp_user" {
  server_id = aws_transfer_server.my_sftp_server.id
  user_name = "tf_test_user"
  role      = aws_iam_role.my_sftp_iam_role.arn
  tags = {
    NAME = "tftestuser"
  }
}

# Create aws transfer ssh
resource "aws_transfer_ssh_key" "my_sftp_transfer" {
  server_id = aws_transfer_server.my_sftp_server.id
  user_name = aws_transfer_user.my_sftp_user.user_name
  body      = "ssh"
}

