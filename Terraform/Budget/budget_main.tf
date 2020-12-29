provider "aws" {
    region = "eu-central-1"
    access_key = var.access_key
    secret_key = var.secret_key
}

resource "aws_budgets_budget" "budget-ec2-monthly" {
    budget_type       = "COST"
    limit_amount      = "5"
    limit_unit        = "USD"
    time_period_start = "2020-09-01_00:00"
    time_unit         = "MONTHLY"

  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = "85"
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = ["xxxxxx@example.com"]
  }
}