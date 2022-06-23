"""Checks ENM GSM cells for baseline parameters."""

from baseline_checker.enm.main import enm_main


def main():
    """Check ENM GSM cells for baseline."""
    print(enm_main('GSM'))


if __name__ == '__main__':
    main()
