output "host-name" {
    value = aws_transfer_server.my_sftp_server.endpoint
}

output "username" {
    value = aws_transfer_user.my_sftp_user.user_name
}