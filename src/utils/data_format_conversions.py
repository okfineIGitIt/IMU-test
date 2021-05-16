EXPECTED_ROTATION_UNITS = ("rad/s", "deg/s")
EXPECTED_ACCELERATION_UNIT = "m/s^2"
EXPECTED_TEMP_UNIT = "degC"


def parse_data_string(data_string):
    data_dict = None

    if not data_string:
        return

    str_to_dict_parsers = [
        parse_rotation_string_to_dict,
        parse_acceleration_string_to_dict,
        parse_temperature_string_to_dict,
    ]

    for parser in str_to_dict_parsers:
        data_dict = parser(data_string)

    if data_dict is None:
        print("Unexpected data string")
        return None

    return data_dict


def parse_rotation_string_to_dict(str_to_parse):
    rot_str_ident = "Rotation"
    data_dict = {"data": rot_str_ident}

    if not str_to_parse.startswith(rot_str_ident):
        return

    unit = None
    for unit_str in EXPECTED_ROTATION_UNITS:
        if unit_str in str_to_parse:
            unit = unit_str

    if unit is None:
        print("Units not provided in rotation string!")

    data_dict["units"] = unit

    str_to_parse = str_to_parse.strip(rot_str_ident)
    str_to_parse = str_to_parse.strip(unit)
    str_to_parse = str_to_parse.replace(" ", "")

    coords = str_to_parse.split(",")
    for coord in coords:
        axis, value = coord.split(":")
        data_dict[axis] = float(value)

    return data_dict


def parse_acceleration_string_to_dict(str_to_parse):
    acc_str_ident = "Acceleration"
    unit = EXPECTED_ACCELERATION_UNIT

    data_dict = {"data": acc_str_ident, "units": unit}

    if not str_to_parse.startswith(acc_str_ident):
        return

    str_to_parse = str_to_parse.strip(acc_str_ident)
    str_to_parse = str_to_parse.strip(unit)
    str_to_parse = str_to_parse.replace(" ", "")

    coords = str_to_parse.split(",")
    for coord in coords:
        axis, value = coord.split(":")
        data_dict[axis] = float(value)

    return data_dict


def parse_temperature_string_to_dict(str_to_parse):
    temp_str_ident = "Temperature"
    unit = EXPECTED_TEMP_UNIT
    data_dict = {"data": temp_str_ident, "units": unit}

    if not str_to_parse.startswith(temp_str_ident):
        return

    str_to_parse = str_to_parse.strip(temp_str_ident + ":")
    str_to_parse = str_to_parse.strip(unit)
    str_to_parse = str_to_parse.replace(" ", "")

    data_dict["temp"] = float(str_to_parse)

    return data_dict


if __name__ == "__main__":
    test_string = "Temperature: 25.28 degC"
    result_dict = parse_data_string(test_string)
    print(result_dict)
