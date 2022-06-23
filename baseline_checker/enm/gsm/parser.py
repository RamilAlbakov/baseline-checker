"""Parse configured on ENM GSM parameters from ENM data."""

import re

parameter_delimeter = ' : '


def parse_fdn(fdn):
    """
    Parse cell name from fdn.

    Args:
        fdn: string

    Returns:
        string
    """
    mo_value_index = -1
    cell_pattern = 'GeranCell=[^,]*'
    cell_mo = re.search(cell_pattern, fdn).group()
    return cell_mo.split('=')[mo_value_index]


def define_cell_band(enm_data):
    """
    Define frequency band for GSM cell.

    Args:
        enm_data: enmscripting ElementGroup

    Returns:
        dict
    """
    cells_by_band = {}
    for element in enm_data:
        element_value = element.value()
        if 'FDN' in element_value:
            cell_name = parse_fdn(element_value)
        elif parameter_delimeter in element_value:
            parameter_value = element_value.split(parameter_delimeter)[-1]
            cells_by_band[cell_name] = parameter_value
    return cells_by_band


def get_parameter_value(cell_name, parameter_name, enm_parameter_val, cells_by_band):
    """
    Get parameter value according to GSM cell frequency band.

    Args:
        cell_name: string
        parameter_name: string
        enm_parameter_val: string
        cells_by_band: dict

    Returns:
        string
    """
    if parameter_name not in {'accMin', 'cro', 'cchPwr'}:
        return enm_parameter_val

    baseline900 = {
        'accMin': '104',
        'cro': '0',
        'cchPwr': '33',
    }

    baseline1800 = {
        'accMin': '94',
        'cro': '8',
        'cchPwr': '30',
    }

    cell_band = cells_by_band[cell_name]
    if cell_band == 'GSM900':
        return (enm_parameter_val, baseline1800[parameter_name])
    elif cell_band == 'GSM1800':
        return (baseline900[parameter_name], enm_parameter_val)


def parse_gsm(enm_gsm_data, cells_by_band):
    """
    Parse GSM parameters from ENM data.

    Args:
        enm_gsm_data: enmscripting ElementGroup
        cells_by_band: dict

    Returns:
        dict with gsm parameters
    """
    enm_gsm_parameters = {}
    for element in enm_gsm_data:
        element_value = element.value()
        if 'FDN' in element_value:
            cell_name = parse_fdn(element_value)
            if cell_name not in enm_gsm_parameters.keys():
                enm_gsm_parameters[cell_name] = {'params': {}}
        elif parameter_delimeter in element_value:
            parameter, parameter_value = element_value.split(parameter_delimeter)
            enm_gsm_parameters[cell_name]['params'][parameter] = get_parameter_value(
                cell_name,
                parameter,
                parameter_value,
                cells_by_band,
            )
    return enm_gsm_parameters
