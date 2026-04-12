def line_parser(line):
    line = line.strip()

    # Split into 3 parts: timestamp|level:severity|message
    parts = [p.strip() for p in line.split("|")]

    if len(parts) != 3:
        raise ValueError("Log Line must have 3 parts: timestamp|level:severity|message")

    timestamp, level_sev, message = parts

    # Validate non-empty fields
    if timestamp == "" or level_sev == "" or message == "":
        raise ValueError("Timestamp/Level:Severity/Message cannot be empty")

    # Split level:severity
    level_sev_parts = [p.strip() for p in level_sev.split(":")]
    if len(level_sev_parts) != 2:
        raise ValueError("Level:Severity must be in the form level:severity")

    #Validate level or severity is not empty
    level, severity_str = level_sev_parts
    if level == "" or severity_str == "":
        raise ValueError("Level and Severity cannot be empty")

    # Validate severity is an integer
    try:
        severity = int(severity_str)
    except ValueError:
        raise ValueError("Severity must be an integer")

    return timestamp, level, severity, message



#Processing log file.
def process_log_file(input_path, warnings_path, errors_path, warning_level="Warning", skip_blank=True):
    total = valid = invalid = warnings = 0
    level_counts = {}

    with open(input_path, "r") as fin, open(warnings_path, "w") as fw, open(errors_path, "w") as fe:
        for line_no, line in enumerate(fin, start=1):
            if skip_blank and not line.strip():
                continue

            total += 1
            try:
                timestamp, level, severity, message = line_parser(line)
            except ValueError as e:
                invalid += 1
                fe.write(f"{line_no}: {e} | raw={line.strip()}\n")
                continue

            valid += 1
            level_counts[level] = level_counts.get(level, 0) + 1

            if level == warning_level:
                warnings += 1
                fw.write(f"{line_no}: {timestamp} | {level}:{severity} | {message}\n")

    return {
        "total": total,
        "valid": valid,
        "invalid": invalid,
        "warnings": warnings,
        "level_counts": level_counts,
    }