from datetime import datetime

def heartbeat(input_file="hblog.txt", output_file="hb_test.log"):
    key = "Key TSTFEED0300|7E3E|0400"
    filtered_lines = []

    with open(input_file) as f:
        for line in f:
            if key in line:
                filtered_lines.append(line.strip())

    log_entries = []

    for i in range(len(filtered_lines) - 1):
        current_line = filtered_lines[i]
        next_line = filtered_lines[i + 1]

        pos_current = current_line.find("Timestamp ")
        pos_next = next_line.find("Timestamp ")

        if pos_current != -1 and pos_next != -1:
            start_cur = pos_current + len("Timestamp ")
            time_str_cur = current_line[start_cur : start_cur + 8]

            start_next = pos_next + len("Timestamp ")
            time_str_next = next_line[start_next : start_next + 8]

            time_cur = datetime.strptime(time_str_cur, "%H:%M:%S")
            time_next = datetime.strptime(time_str_next, "%H:%M:%S")

            diff = (time_cur - time_next).total_seconds()

            if 31 < diff < 33:
                log_entries.append(
                    f"WARNING: Heartbeat {int(diff)}s at {time_str_cur}"
                )
            elif diff >= 33:
                log_entries.append(
                    f"ERROR: Heartbeat {int(diff)}s at {time_str_cur}"
                )

    with open(output_file, "w", encoding="utf-8") as f_out:
        for entry in log_entries:
            f_out.write(entry + "\n")

    print(f"{len(log_entries)} messages logs are in '{output_file}'.")


if __name__ == "__main__":
    heartbeat()