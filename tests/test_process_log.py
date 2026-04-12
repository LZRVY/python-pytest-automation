from src.log_utils import process_log_file

def test_process_log_file_pipeline(tmp_path):
    #Temporary Paths for the input/output files
    log_file_path = tmp_path / "log.txt"
    warnings_file_path = tmp_path / "warnings.txt"
    errors_file_path = tmp_path / "errors.txt"

    #Write log_lines into log_file_path
    lines = ["040726-210822|Critical:1|Emergency message",
        "040726-210822|Error:2|Payment failed",
        "040726-210822|Warning:3|Disk usage high",
        "040726-210822|Debug:5|Debug details",
        "THIS IS A BROKEN LINE",                      # invalid (no pipes)
        "040726-210822|Trace:6|Trace details",
        "040726-210822|Informational:4|Tax rate computed",
        "040726-210822|Warning:3|Another warning",     # valid warning
        "040726-210822|Warning:3|",                    # invalid (empty message)
        "040726-210822|Error:2|Another error",
    ]
    log_file_path.write_text("\n".join(lines) + "\n")

    summary = process_log_file(log_file_path,
                               warnings_file_path,
                               errors_file_path,
                               warning_level = "Warning",
                               skip_blank=True)

    #Assert Summary Counts
    assert summary["total"] == 10
    assert summary["valid"] == 8
    assert summary["invalid"] == 2
    assert summary["warnings"] == 2

    # Verify warning.txt should contain only warnings
    warnings_lines = warnings_file_path.read_text().strip().splitlines()
    assert len(warnings_lines) == 2
    assert all ("Warning:" in line for line in warnings_lines)

    # Verify error.txt should only contain broken, and empty lines.
    error_text = errors_file_path.read_text()
    assert "THIS IS A BROKEN LINE" in error_text
    assert "empty" in error_text.lower()