import itertools
import time

def log_line_generator(levels, messages, severities, n=30,
                       bad_no_pipe_at = None, bad_empty_message = None):

    pairs = itertools.islice(zip(itertools.cycle(levels), itertools.cycle(messages)),n)
    bad_no_pipe_at = set() if bad_no_pipe_at is None else set(bad_no_pipe_at)
    bad_empty_message = set() if bad_empty_message is None else set(bad_empty_message)

    for idx, (level,message) in enumerate(pairs):
        timestamp = time.strftime("%m%d%y-%H%M%S")
        severity = severities[level]

        if idx in bad_empty_message:
            severity = severities[level]
            yield f"{timestamp}|{level}:{severity}|"

        if idx in bad_no_pipe_at:
            yield "THIS IS A BROKEN LINE"
            continue

        yield f"{timestamp}|{level}:{severity}|{message}"
