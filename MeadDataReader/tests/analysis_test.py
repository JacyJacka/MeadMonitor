import unittest
from unittest.mock import patch
from MeadDataReader.Modules.data_analysis import Plot_data_and_regression


class PlotDataAndRegressionTests(unittest.TestCase):

    def setUp(self):
        self.x = list(range(100))
        self.y = [2.0 * x + 1.0 for x in self.x]  # y = 2x + 1, known params

    @patch('MeadDataReader.Modules.data_analysis.plt')
    def test_no_regression_returns_none(self, mock_plt):
        popt, cov = Plot_data_and_regression(self.x, self.y, regression_size=0)
        self.assertIsNone(popt)
        self.assertIsNone(cov)

    @patch('MeadDataReader.Modules.data_analysis.plt')
    def test_regression_returns_correct_params(self, mock_plt):
        popt, cov = Plot_data_and_regression(self.x, self.y, regression_size=50)
        self.assertAlmostEqual(float(popt[0]), 2.0, places=5)
        self.assertAlmostEqual(float(popt[1]), 1.0, places=5)

    @patch('MeadDataReader.Modules.data_analysis.plt')
    def test_regression_size_larger_than_data_does_not_crash(self, mock_plt):
        popt, cov = Plot_data_and_regression(self.x, self.y, regression_size=9999)
        self.assertIsNotNone(popt)
        self.assertIsNotNone(cov)

    @patch('MeadDataReader.Modules.data_analysis.plt')
    def test_plot_and_show_are_called(self, mock_plt):
        Plot_data_and_regression(self.x, self.y)
        mock_plt.plot.assert_called()
        mock_plt.show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
