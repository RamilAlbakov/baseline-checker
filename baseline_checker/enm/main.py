"""Checks ENM cells for baseline parameters."""

from baseline_checker.enm.gsm.compare import compare_gsm_baseline
from baseline_checker.enm.gsm.excel import fill_gsm_report
from baseline_checker.enm.gsm.gsm_enm import GsmEnm
from baseline_checker.enm.gsm.parser import define_cell_band, parse_gsm
from dotenv import load_dotenv

load_dotenv('.env')


def enm_main(technology):
    """
    Check ENM cells for baseline parameters.

    Args:
        technology: string
    """
    if technology == 'GSM':
        enm_bscs = ['AKTA_B1']
        for enm_bsc in enm_bscs:
            bsc = GsmEnm(enm_bsc)
            enm_bsc_data = bsc.execute_enm_command(bsc.cli_command)
            enm_bsc_band_data = bsc.execute_enm_command(bsc.freq_band_cli_command)
            cells_by_band = define_cell_band(enm_bsc_band_data)
            gsm_params = parse_gsm(enm_bsc_data, cells_by_band)
            params_diff, inconsistencies_stat = compare_gsm_baseline(gsm_params, bsc.baseline)
            fill_gsm_report(bsc.bsc, params_diff, bsc.baseline, cells_by_band)
