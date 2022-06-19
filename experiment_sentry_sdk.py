import sentry_sdk

sentry_sdk.init(
    dsn="https://test:test@gentry.con2.fi/1",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

raise Exception("Sinä olet kakkapylly")
