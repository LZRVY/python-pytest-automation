import src.log_utils as utils
import src.log_line_generator as gen

if __name__ == "__main__":
    levels = ["Critical",
              "Error",
              "Warning",
              "Debug",
              "Informational",
              "Trace"]
    messages = ["**Emergency** Connection to primary database lost; shutting down server.",
                "Failed to process payment for User #8821 due to timeout.",
                "Disk usage at 85%; cleanup recommended to avoid latency.",
                "User 'LZRVY' successfully logged in from IP 192.168.1.1.",
                "Calculated tax rate for Order #442: 0.075 based on zip code 90210.",
                "Entering 'validate_token' function with arguments: (token_str='abc123', ttl=3600)."]

    severities = {"Critical": 1,
                  "Error": 2,
                  "Warning": 3,
                  "Informational": 4,
                  "Debug": 5,
                  "Trace": 6}

    with open("../data/log.txt", "w") as f:
        for line in gen.log_line_generator(levels,
                                           messages,
                                           severities,
                                           n=30,
                                           bad_no_pipe_at={4},
                                           bad_empty_message={16}):
            print(line)
            f.write(line + "\n")

    summary = utils.process_log_file("../data/log.txt", "../data/warning.txt", "../data/error.txt")
    print(summary)
