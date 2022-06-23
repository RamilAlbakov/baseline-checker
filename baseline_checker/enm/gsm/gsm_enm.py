"""Get GSM cell data from ENM by executing ENM CLI commands."""

from baseline_checker.enm.enm import Enm


class GsmEnm(Enm):
    """Get ENM GSM cells parameters by executing ENM CLI commands."""

    baseline = {
        'clsState': 'ACTIVE',
        'clsLevel': '20',
        'clsAcc': '40',
        'hoClsAcc': 'ON',
        'rHyst': '75',
        'clsRamp': '8',
        'chap': '1',
        'csPsAlloc': 'CSFIRSTPSLAST',
        'gprsPrio': '0',
        'primpLim': '8',
        'pdchPreempt': '0',
        'sPdch': '0',
        'dtHAmr': '30',
        'dtHNAmr': '20',
        'dhaSs': 'OFF',
        'dhaSsThraSs': '96',
        'dhaSsThrHo': '98',
        'irc': 'ON',
        'prachBlk': '2',
        'pskOnBcch': 'YES',
        'chCsDl': 'CS2',
        'intAve': '25',
        'limit1': '3',
        'limit2': '8',
        'limit3': '13',
        'limit4': '18',
        'accMin': ('104', '94'),
        'crh': '6',
        'cro': ('0', '8'),
        'maxRet': '2',
        'agBlk': '1',
        'mFrms': '4',
        'isHoLev': '0',
        'qsc': '15',
        'qsci': 'QSEARCH_I',
        'qsi': '7',
        'fddMrr': '1',
        'fddQMin': '6',
        'fddQOff': '0',
        'fastRet3g': 'ACTIVE',
        'eInitMcs': '3',
        'la': 'ON',
        'iho': 'ON',
        'maxIHo': '2',
        'tMaxiHo': '7',
        'tiHo': '10',
        'pSsBq': '10',
        'pSsHf': '10',
        'pTimBq': '7',
        'pTimHf': '7',
        'pSsTa': '63',
        'pTimTa': '30',
        'qLimDlAfr': '65',
        'qLimUlAfr': '65',
        'qLimDl': '55',
        'qLimUl': '55',
        'cellQ': 'HIGH',
        'mbcr': 'SIX',
        'aw': 'ON',
        'hystSep': '-90',
        'hpbState': 'ACTIVE',
        'amrPcState': 'ACTIVE',
        'ssDesDlAfr': '90',
        'dtxD': 'ON',
        'ssDesDl': '92',
        'qDesDl': '35',
        'lCompDl': '5',
        'qCompDl': '73',
        'qDesDlAfr': '40',
        'ssDesDlAhr': '90',
        'qDesDlAhr': '35',
        'ssDesDlAwb': '90',
        'qDesDlAwb': '30',
        'cchPwr': ('33', '30'),
        'msRxMin': '100',
        'dtxU': 'USE',
        'gamma': '20',
        'ssDesUl': '92',
        'qDesUl': '30',
        'lCompUl': '5',
        'qCompUl': '73',
        'ssDesUlAfr': '90',
        'qDesUlAfr': '40',
        'ssDesUlAhr': '90',
        'qDesUlAhr': '35',
        'ssDesUlAwb': '92',
        'qDesUlAwb': '30',
        'rLinkUp': '32',
        'rLinkT': '32',
        'rLinkTaFr': '32',
        'rLinkTaHr': '32',
        'rLinkTAwb': '32',
        'eFactor': '2',
    }

    gsm_parameters = {
        'ChannelAllocAndOpt': 'chap,csPsAlloc,gprsPrio,primpLim,pdchPreempt,sPdch',
        'CellLoadSharing': 'clsState,clsLevel,clsAcc,hoClsAcc,rHyst,clsRamp',
        'DynamicHrAllocation': 'dtHAmr,dtHNAmr,dhaSs,dhaSsThraSs,dhaSsThrHo',
        'GeranCell': 'irc',
        'Gprs': 'prachBlk,pskOnBcch,chCsDl',
        'IdleChannelMeasurement': 'intAve,limit1,limit2,limit3,limit4',
        'IdleModeAndPaging': 'accMin,crh,cro,maxRet,agBlk,mFrms',
        'InterRanMobility': 'isHoLev,qsc,qsci,qsi,fddMrr,fddQMin,fddQOff,fastRet3g',
        'LinkQualityControl': 'eInitMcs,la',
        'LocatingIntraCellHandover': 'iho,maxIHo,tMaxiHo,tiHo',
        'LocatingPenalty': 'pSsBq,pSsHf,pTimBq,pTimHf,pSsTa,pTimTa',
        'LocatingUrgency': 'qLimDlAfr,qLimUlAfr,qLimDl,qLimUl,cellQ',
        'Mobility': 'mbcr,aw,hystSep',
        'PowerControl': 'hpbState,amrPcState',
        'PowerControlDownlink': 'ssDesDlAfr,dtxD,ssDesDl,qDesDl,lCompDl,qCompDl,qDesDlAfr,ssDesDlAhr,qDesDlAhr,ssDesDlAwb,qDesDlAwb',
        'PowerControlUplink': 'cchPwr,msRxMin,dtxU,gamma,ssDesUl,qDesUl,lCompUl,qCompUl,ssDesUlAfr,qDesUlAfr,ssDesUlAhr,qDesUlAhr,ssDesUlAwb,qDesUlAwb',
        'RadioLinkTimeout': 'rLinkUp,rLinkT,rLinkTaFr,rLinkTaHr,rLinkTAwb',
        'TbfReservation': 'eFactor',
    }

    def __init__(self, bsc):
        """
        Construct bsc instance.

        Args:
            bsc: string
        """
        self.bsc = bsc

    @property
    def cli_command(self):
        """
        Create ENM CLI command to get neccessary parameters for GSM cells.

        Returns:
            string
        """
        mo_filters = [
            f'{mo_type}.({mo_params})' for mo_type, mo_params in self.gsm_parameters.items()
        ]
        cli_filter = ';'.join(mo_filters)
        return 'cmedit get {scope} {cli_filter}'.format(scope=self.bsc, cli_filter=cli_filter)

    @property
    def freq_band_cli_command(self):
        """
        Create ENM CLI command to get GSM frerquency band data.

        Returns:
            string
        """
        return 'cmedit get {scope} GeranCell.(cSysType)'.format(scope=self.bsc)
