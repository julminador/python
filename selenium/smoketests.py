from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner # Genera el reporte
from assertions import AssertionsTest
from searchtests import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

# Suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])

# Genera reporters
kwargs = {
    "output": 'smoke-report'
    }

# Almacena el reporte generado por HTMLTestRuner
runner = HTMLTestRunner(**kwargs)

# Ejecuta rurner con la suite de prueba
runner.run(smoke_test) 