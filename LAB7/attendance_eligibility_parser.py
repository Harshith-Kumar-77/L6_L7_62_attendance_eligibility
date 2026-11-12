def normalize_srn(srn):
    """
    Trims and upper-cases a student registration number.
    Safely handles None, non-strings, and empty/whitespace strings without crashing.
    """
    if not isinstance(srn, str):
        return ""
    cleaned = srn.strip().replace(' ', '').upper()
    if not cleaned:
        return ""
    return cleaned


def attendance_from_ratio(text):
    """
    Converts 'ATTENDED/HELD' into a whole-number percentage (0-100).
    Safely handles None, malformed formats, non-integers, negative numbers,
    attended > held, and zero held classes without crashing.
    """
    if not isinstance(text, str) or '/' not in text:
        return 0

    parts = text.split('/')
    if len(parts) != 2:
        return 0

    try:
        attended = int(parts[0].strip())
        held = int(parts[1].strip())
    except ValueError:
        return 0

    if held <= 0 or attended < 0 or attended > held:
        return 0

    return attended * 100 // held


def attendance_from_register(marks):
    """
    Works out the attendance percentage from a string of P (present) and A (absent).
    Safely handles None, empty strings, and invalid characters without crashing.
    """
    if not isinstance(marks, str):
        return 0

    cleaned = marks.strip().replace(' ', '').upper()
    if not cleaned:
        return 0

    # Ensure all characters are strictly 'P' or 'A'
    if any(ch not in ('P', 'A') for ch in cleaned):
        return 0

    return cleaned.count('P') * 100 // len(cleaned)


def main():
    print("==== Running normalize_srn ====")
    value = input("Enter an SRN (e.g. pes1ug23cs001): ")
    print("Normalized SRN:", normalize_srn(value))

    print("\n==== Running attendance_from_ratio ====")
    value = input("Enter classes attended and held as ATTENDED/HELD (e.g. 30/40): ")
    print("Attendance percent:", attendance_from_ratio(value))

    print("\n==== Running attendance_from_register ====")
    value = input("Enter the register as P/A marks (e.g. PPAPP): ")
    print("Attendance percent:", attendance_from_register(value))


if __name__ == "__main__":
    main()