def format_number(num):
    try:
        if num is None:
            return None

        if num >= 1_00_00_00_000:  # Crores
            return f"₹{round(num/1_00_00_00_000, 1)}L Cr"
        elif num >= 1_00_00_000:
            return f"₹{round(num/1_00_00_000, 1)}Cr"
        elif num >= 1_00_000:
            return f"₹{round(num/1_00_000, 1)}L"
        elif num >= 1_000:
            return f"{round(num/1_000, 1)}K"
        return str(num)
    except:
        return str(num)