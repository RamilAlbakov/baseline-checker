"""Compares GSM parameters from ENM with baseline."""

from dictdiffer import diff


def count_inconsistencies(gsm_cells_num, baseline_parameters_num, gsm_diff):
    """
    Count the number of inconsistencies.

    Args:
        gsm_cells_num: int
        baseline_parameters_num: int
        gsm_diff: dict

    Returns:
        tuple
    """
    bsc_parameters_num = gsm_cells_num * baseline_parameters_num
    inconsistencies_count_list = [
        len(inconsistencies.keys()) for inconsistencies in gsm_diff.values()
    ]
    return (sum(inconsistencies_count_list), bsc_parameters_num)


def compare_gsm_baseline(enm_gsm_parameters, gsm_baseline):
    """
    Compare GSM parameters from ENM with baseline.

    Args:
        enm_gsm_parameters: dict
        gsm_baseline: dict

    Returns:
        dict of parameter difference
    """
    gsm_diff = {}
    for cell_name, cell_params in enm_gsm_parameters.items():
        cell_delta = list(diff(cell_params['params'], gsm_baseline))
        gsm_diff[cell_name] = {}
        for changed_parameter in cell_delta:
            parameter, parameter_diff = changed_parameter[1:]
            gsm_diff[cell_name][parameter] = parameter_diff

    inconsistencies_stat = count_inconsistencies(
        len(enm_gsm_parameters.keys()),
        len(gsm_baseline.keys()),
        gsm_diff,
    )
    return (gsm_diff, inconsistencies_stat)
