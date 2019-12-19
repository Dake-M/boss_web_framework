# -*- coding: utf-8 -*-
import pytest
import warnings

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    pytest.main(["--html=Outputs/reports/report.html"])
    # pytest.main(["-m", "demo", "--reruns", "2", "--reruns-delay", "5", "--html=Outputs/reports/report.html"])